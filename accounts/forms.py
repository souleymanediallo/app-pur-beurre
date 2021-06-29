from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser
from .models import Profile


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ["email", "username", "password1", "password2"]


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = CustomUser
        fields = ["username", "email"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["image", "description"]