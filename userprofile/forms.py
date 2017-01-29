from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

from userprofile.models import UserProfile


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password']
        labels = {
            'email': "E-posta",
            'username': "Kullanıcı Adı",
            'password': "Parola"
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-posta', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Parola', 'class': 'form-control'})
        }


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username']
        labels = {
            'email': "E-posta",
            'username': "Kullanıcı Adı"
        }
        widgets = {
            'email': forms.TextInput(attrs={'placeholder': 'E-posta', 'class': 'form-control'}),
            'username': forms.TextInput(attrs={'placeholder': 'Kullanıcı Adı', 'class': 'form-control'})
        }


class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_photo']
        labels = {
            'profile_photo': "Profil Fotoğrafı"
        }
