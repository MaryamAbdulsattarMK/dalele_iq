from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .models import postInfo
from .views import PostAPIView,PostTimeDetailAPIView,locationAPIView,locationAPIViewUP,PostDetailAPIView,SaveFile
urlpatterns = [
    path('Post/GetPostinfo',PostAPIView.as_view(),name='get Post'),
    path('post/Postinfo_GPUD/<int:id>', PostDetailAPIView.as_view(), name='updatepost'),
    path('post/Post_History', PostTimeDetailAPIView.as_view(), name='Post_History'),
    path('post/Location/<int:id>', locationAPIView.as_view(), name='location'),
    path('post/Location', locationAPIViewUP.as_view(), name='RegionAPIView'),

    path('save', SaveFile, name='Post_Detail')


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)