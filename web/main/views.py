from django.shortcuts import render
from .models import Photos

def index(response):
    photos = Photos.objects.all() #zasysa wszystkie dane z bazy danych
    context = {
        'photos': photos,
    }
    return render(response, "main/base.html", context)
