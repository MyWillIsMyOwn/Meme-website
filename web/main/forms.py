from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "confirm password"}
        )
    )

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        widgets = {
            "email": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "email"}
            ),
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "username"}
            ),
        }


class LoginUserForm(UserCreationForm):
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "password"}
        )
    )

    class Meta:
        model = User
        fields = ["username", "password"]
        widgets = {
            "username": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "username"}
            ),
        }
