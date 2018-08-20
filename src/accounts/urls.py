from django.urls import path , re_path 
from .views import register, edit, activate, account_activation_sent
urlpatterns = [
    path('register/', register, name='register'),
    path('edit/', register, name='edit'),
    path('activate/<slug:uidb64>/<slug:token>)/', activate, name='activate'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
    
]
