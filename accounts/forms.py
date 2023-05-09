from django.forms import ModelForm
from django import forms
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Blogform(ModelForm):
    title = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    description = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Blog
        fields = '__all__'


class CoustomUserRagister(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Email'}))
    password1 = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'password', 'class': 'form-control', 'placeholder': 'Confirm Password'}))

    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2'
        ]
