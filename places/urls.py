from django.urls import path

from .views import places_list

urlpatterns = [
    path('', places_list, name='place-list'),
]
