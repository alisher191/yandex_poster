from django.contrib import admin

from .models import Place, PlaceImages


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(PlaceImages)
class PlaceImagesAdmin(admin.ModelAdmin):
    list_display = ['title']
