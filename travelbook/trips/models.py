from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from tinymce.models import HTMLField
from PIL import Image


class Trip(models.Model):
    title = models.CharField(max_length=250, null=False, blank=False)
    owner = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='trips', null=True, blank=True)

    def __str__(self):
        return self.title


class Place(models.Model):
    name = models.CharField(max_length=250, null=False, blank=False)
    date = models.DateField(null=True, blank=True)
    trip = models.ForeignKey(Trip, null=False, blank=False, on_delete=models.CASCADE, related_name='places')
    content = HTMLField(blank=True, null=True)
    image = models.ImageField(upload_to = 'trips/images/', blank=True, null=True)

    def __str__(self):
        return self.name

 
class PlaceImage(models.Model):
    place = models.ForeignKey(Place, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'trips/images/', blank=True, null=True)

    def __str__(self):
        return self.place.name

