from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, null=True, blank=True)
    is_email_confirmed = models.BooleanField(default=False)