from django.contrib.auth import login, authenticate
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib import messages
from django.core.mail import EmailMessage
from django.template.loader import render_to_string


from .forms import  RegistrationForm,UserProfileForm 
from .tokens import email_activation_token

from .models import Profile
from django.contrib.auth.models import User

def home(request):
    return render(request, 'accounts/home.html', {})



def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
             #hash password
            new_user.set_password(user_form.cleaned_data['password1'])
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user)

            if new_user.profile.is_email_confirmed:
                #send one time activation email
                current_site = get_current_site(request)
                subject = 'Activate Account'
                sender = 'achiengcindy36@gmail.com'
                message = render_to_string('accounts/account_activation_email.html', {
                    'user':  new_user,
                    'domain': current_site.domain,
                    'uid':urlsafe_base64_encode(force_bytes( new_user.pk)).decode(),
                    'token':email_activation_token.make_token( new_user),
                })
                 # https://stackoverflow.com/questions/40655802/how-to-implement-email-user-method-in-custom-user-model
                NEW_user.email_user(subject, message)
                return redirect('account_activation_sent')
            
            else:
                return redirect('login')


    else:
        user_form = RegistrationForm()
    return render(request, 'accounts/register.html',{'user_form': user_form})
  


def account_activation_sent(request):
    return render(request, 'accounts/account_activation_sent.html')


def activate(request, uidb64, token, backend='accounts.authentication.EmailAuthBackend'):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and email_activation_token.check_token(user, token):
        user.is_active = True
        user.is_email_confirmed = True
        user.save()
        login(request, user, 'accounts.authentication.EmailAuthBackend')
        return redirect('qr')


@login_required
def edit(request):
    if request.method == 'POST':
        edit_form = ProfileEditForm(instance=request.user.profile ,data=request.POST)
        if edit_form.is_valid():
            request.user.is_active = False
            edit_form.save()
            #send one time activation email
            current_site = get_current_site(request)
            subject = 'Email Confirmation'
            sender = 'achiengcindy36@gmail.com'
            message = render_to_string('accounts/account_activation_email.html', {
                'user':  request.user,
                'domain': current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes( request.user.pk)).decode(),
                'token':email_activation_token.make_token( request.user),
            })
            # https://stackoverflow.com/questions/40655802/how-to-implement-email-user-method-in-custom-user-model
            email = EmailMessage(subject, message,sender, [request.user.email])
            email.send()
            return redirect('account_activation_sent')
            print(request, 'Email updated successfully')
        else:
            print(request, 'Error updating your profile')
    else:
        edit_form = ProfileEditForm(instance=request.user)
    return render(request,'accounts/edit.html',{'edit_form': edit_form})






