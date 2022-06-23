from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import Users


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = Users
        fields = ["username", "svd"]


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = Users
        fields = ["username", "svd"]