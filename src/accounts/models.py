
from django.db import models
from django.contrib.auth.models import User
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user' , on_delete=models.CASCADE,)
