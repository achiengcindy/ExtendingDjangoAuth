from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User

class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username','email','first_name')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)

class LoginForm(forms.Form):
    username = forms.CharField(label = 'username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

 







