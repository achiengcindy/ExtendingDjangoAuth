from django import forms
from django.contrib.auth.models import User

from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(label = "Email", required = False)

    class Meta:
        model = User
        fields = ("username", "password1", "password2")

        def clean_email(self):
            email = self.cleaned_data['email']
            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('That email is already taken')
            return email

   


""" class RegistrationForm(forms.Form):
    username = forms.CharField(label= "username", widget=forms.TextInput, required = True)
    email = forms.EmailField(label = "Email", required = False)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput, required = True)
    password2 = forms.CharField(label='confirm password', widget=forms.PasswordInput, required = True)

    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('That email is already taken')
        return email

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('Please use another username,that is already taken')
        return username
    
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
 """
    



