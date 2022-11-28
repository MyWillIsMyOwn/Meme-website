from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload, name="upload"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_user, name="home"),
    path("register/", views.register_page, name="register_page"),
]
