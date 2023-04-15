from django.core.files.storage import default_storage
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from .serializer import PostForSerializer, postDetailSerialzer,locationSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView

from .models import postInfo, PostDetail,location
from django_filters.rest_framework import DjangoFilterBackend

class PostAPIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostForSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'location']
    search_feilds = ['title', 'location']
    ordering_feilds = ['title', 'location']

    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return postInfo.objects.filter()



class PostDetailAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = PostForSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return postInfo.objects.filter()

class PostTimeDetailAPIView(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = postDetailSerialzer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id','created_at','updated_at']
    search_feilds = ['id','created_at','updated_at']
    ordering_feilds = ['id','created_at','updated_at']


    def get_queryset(self):
        return PostDetail.objects.defer("id", 'created_at', 'updated_at')


class locationAPIView(RetrieveUpdateDestroyAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = locationSerializer
    lookup_field = 'id'

    def get_queryset(self):
        return location.objects.filter()


class locationAPIViewUP(ListCreateAPIView):
    """This endpoint list all of the available todos from the database"""
    permission_classes = (IsAuthenticated,)  # permission classes
    serializer_class = locationSerializer


    def perform_create(self, serializer):
        return serializer.save()

    def get_queryset(self):
        return location.objects.filter()

@csrf_exempt
def SaveFile(request):
    file = request.FILES['image']
    file_name = default_storage.save(file.name, file)
    return JsonResponse(file_name, safe=False)
