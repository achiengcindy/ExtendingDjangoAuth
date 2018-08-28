from django.urls import path 
from .views import register, home, edit, activate, account_activation_sent

urlpatterns = [
	path('', home, name='home'),
    path('register/', register, name='register'),
    path('edit/', edit, name='edit'),
    path('activate/<slug:uidb64>/<slug:token>)/', activate, name='activate'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent')  
]
