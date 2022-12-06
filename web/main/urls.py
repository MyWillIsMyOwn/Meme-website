from django.urls import path

from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("upload/", views.upload, name="upload"),
    path("login/", views.login_page, name="login_page"),
    path("logout/", views.logout_user, name="logout"),
    path("register", views.register_page, name="register_page"),
    path("meme/<str:id>/", views.meme, name="meme"),
    path("like/<int:pk>", views.like, name="like_post"),
    path("comment/<int:pk>", views.comment, name="comment_post"),
]
