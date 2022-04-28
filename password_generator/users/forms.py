from dataclasses import field
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import PasswordModel

class PasswordForm(forms.ModelForm):
    class Meta:
        model = PasswordModel
        fields = ('platform', 'password')