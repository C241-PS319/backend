from datetime import datetime, timedelta
from django.db import models
from django.contrib.auth.models import AbstractUser
from app.authentication.constants import DEFAULT_USER_PICTURE

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    picture = models.URLField(default=DEFAULT_USER_PICTURE)
    phone = models.CharField(max_length=20, default="")
    
    REQUIRED_FIELDS = ['name', 'email', 'password', 'phone']

    def __str__(self):
        return self.email