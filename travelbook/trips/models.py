from django.db import models
from tinymce.models import HTMLField
from PIL import Image


class Trip(models.Model):
    title = models.CharField(max_length=250)
 
    def __str__(self):
        return self.title


class Place(models.Model):
    name = models.CharField(max_length=250)
    date = models.DateField(null=True, blank=True)
    trip = models.ForeignKey(Trip, default=None, on_delete=models.CASCADE, related_name='places')
    description = models.TextField()
    # description = HTMLField(blank=True, null=True)
    image = models.FileField(blank=True)
 
    def __str__(self):
        return self.name

 
class PlaceImage(models.Model):
    place = models.ForeignKey(Place, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'trips/images/')

    def save(self):
        super().save()

        img = Image.open(self.images.path)

        if img.height > 300 or img.width > 300:
            new_img = (300, 300)
            img.thumbnail(new_img)
            img.save(self.images.path)

    def __str__(self):
        return self.place.name
