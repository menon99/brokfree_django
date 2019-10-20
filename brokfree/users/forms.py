from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class signupform(UserCreationForm):
    first_name=forms.CharField(max_length=30)
    last_name=forms.CharField(max_length=30)
    mobile=forms.CharField(max_length=10)

    class Meta:
        model=User
        fields=('username','first_name','last_name','mobile','email','password1','password2')

class loginform(forms.Form):
    email=forms.CharField()
    password=forms.CharField()