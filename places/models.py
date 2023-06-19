from django.db import models
from ckeditor.fields import RichTextField


class Place(models.Model):
    title = models.CharField(max_length=100)
    content = RichTextField()

    def __str__(self) -> str:
        return self.title

