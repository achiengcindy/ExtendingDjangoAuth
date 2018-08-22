from django.urls import path 
from .views import register, home,user_login, edit, activate, account_activation_sent

app_name = 'accounts'
urlpatterns = [
	path('', home, name='home'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('edit/', edit, name='edit'),
    path('activate/<slug:uidb64>/<slug:token>)/', activate, name='activate'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent')  
]
