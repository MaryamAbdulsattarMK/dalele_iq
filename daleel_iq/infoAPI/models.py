from datetime import timedelta

from django.db import models
from django.utils import timezone

from helpers import models as modul




class location(models.Model):
    id = models.AutoField(primary_key=True)
    City = models.CharField(max_length=255)
    latitude=models.FloatField()
    longitude=models.FloatField()
    def __str__(self):
        return self.City



def in_three_days():
    return timezone.now() + timedelta(days=3)


class PostDetail(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    expierd_at = models.DateTimeField(default=in_three_days)
    edits_time = models.IntegerField(default=1)
    view=models.IntegerField(default=0)
    liked=models.IntegerField(default=0)
    shared=models.IntegerField(default=0)



class postInfo(modul.TrackingModel):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=250)
    image = models.ImageField(upload_to='photo/%y/%m/%d',default='default/1.png')
    location = models.ForeignKey(location, on_delete=models.CASCADE)
    Phone_number = models.IntegerField(default=12345678)
    Date = models.DateField(auto_created=True,default=timezone.now)
    PostDetail = models.OneToOneField(PostDetail, on_delete=models.CASCADE)

    def __str__(self):
        return self.Name



