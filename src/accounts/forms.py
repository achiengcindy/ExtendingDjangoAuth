from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Profile


class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username','email', 'password1', 'password2',)



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

 






