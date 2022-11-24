from django.shortcuts import render
from .models import Photos
from django.core.paginator import Paginator


def index(response):
    photos = Photos.objects.all()  # zasysa wszystkie dane z bazy danych

    pagination = Paginator(photos, 2)
    page = response.GET.get("page")
    single_page = pagination.get_page(page)
    context = {
        "photos": photos,
        "single_page": single_page,
    }
    return render(response, "main/base.html", context)
