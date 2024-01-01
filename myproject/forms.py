from django import forms
from . models import Vehicles,Category,Profiles

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class Registerform(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter Username',
            'class':'form-control'
        }
    ))
    email=forms.CharField(widget=forms.EmailInput(
        attrs={
            'placeholder': 'Enter Email id',
            'class':'form-control'
        }
    ))
    password1=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter password',
            'class':'form-control'
        }
    ))
    password2=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'placeholder': 'Enter password again',
            'class':'form-control'
        }
    ))
    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter Firstname',
            'class':'form-control'
        }
    ))
    last_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': 'Enter Lastname',
            'class':'form-control'
        }
    ))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model=Profiles
        fields='__all__'


class VehicleForm(forms.ModelForm):
    class Meta:
        model=Vehicles
        fields='__all__'


class CategoryForm(forms.ModelForm):
    class Meta: 
        model=Category
        fields='__all__'