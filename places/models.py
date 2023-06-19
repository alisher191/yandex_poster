from django.db import models
from ckeditor.fields import RichTextField


class Place(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()
    image = models.ManyToManyField('PlaceImages', null=True, blank=True)


    def __str__(self) -> str:
        return self.title


class PlaceImages(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='place_images/')

    def __str__(self) -> str:
        return self.title
