from django.shortcuts import render, redirect, get_object_or_404
from .models import Photos, Comment
from django.core.paginator import Paginator
from .forms import CreateUserForm, LoginUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse

# response is an http request, like POST, GET etc.

# @login_required(login_url='login') <- put decorator above functions that requires being loged in


def home(response):
    photos = Photos.objects.all()  # collect all data from database
    pagination = Paginator(photos[::-1], 3)
    page = response.GET.get("page")
    single_page = pagination.get_page(page)
    context = {
        "single_page": single_page,
    }
    return render(response, "main/main.html", context)


def login_page(response):
    form = LoginUserForm()
    if response.method == "POST":
        username = response.POST.get("username")
        password = response.POST.get("password")
        user = authenticate(response, username=username, password=password)
        if user is not None:
            login(response, user)
            return redirect("/")
        else:
            messages.info(response, "Username or password is incorrect")

    context = {"user_login_form": form}
    return render(response, "main/login.html", context)


def logout_user(response):
    logout(response)
    return redirect("/")


# if inputed data and they are correct save user, otherwise show page
def register_page(response):
    form = CreateUserForm()
    if response.method == "POST":
        form = CreateUserForm(response.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get("username")
            messages.success(response, "Account was created for: " + user)
            return redirect("/login/")
    context = {"user_creation_form": form}
    return render(response, "main/register.html", context)


@login_required(login_url="/login")
def upload(response):
    if response.method == "POST":
        data = response.POST
        image = response.FILES.get("Browser")

        Photos.objects.create(
            title=data["Title"], owner=data["Username"], picture=image
        )
        return redirect("/")
    return render(response, "main/upload.html", {})


@login_required(login_url="/login")
def meme(response, id):
    photo = Photos.objects.get(id=id)
    context = {"photo": photo}
    return render(response, "main/single.html", context)


def like(response, pk):
    photo = get_object_or_404(Photos, id=response.POST.get("photo_id"))
    if response.user in photo.likes.all():
        photo.likes.remove(response.user)
    else:
        photo.likes.add(response.user)
    print("response.get_host()", photo.id)
    return HttpResponseRedirect(reverse("meme", args=[int(pk)]))


def comment(response, pk):
    if response.method == "POST":
        data = response.POST
        Comment.objects.create(
            photo=Photos.objects.get(id=pk),
            owner_name=data["Username"],
            body=data["Comment"],
        )
    return HttpResponseRedirect(reverse("meme", args=[int(pk)]))
