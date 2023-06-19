from django.shortcuts import render

from .models import Place

def places_list(request):
    places = Place.objects.all()
    return render(request, 'index.html', context={'places': places})
