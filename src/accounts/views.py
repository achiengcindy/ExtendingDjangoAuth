from django.contrib.auth import login
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage

from .forms import RegistrationForm



""" def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object.Just don't save it yet
            #new_user = user_form.save(commit=False)
            username = user_form.cleaned_data['username']
            email = user_form.cleaned_data['email']
            #hash password
            raw-password = form.cleaned_data.get('password1')
            # save the new user object
            #new_user.save()
            user = User.objects.create_user(username, email, raw-password)
            user.save()
            return render(request,'registration/login.html')
    else:
        user_form = RegistrationForm()
    return render(request, 'accounts/register.html',{'user_form': user_form})
 """

def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            email = user_form.cleaned_data['email']
            # Gashpassword
            # new_user.set_password(user_form.cleaned_data['password'])
            user_form.save()
            return render(request,'registration/login.html')

    else:
        user_form = RegistrationForm

    return render(request, 'accounts/register.html',{'user_form': user_form})