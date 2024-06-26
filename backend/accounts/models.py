from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .manager import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=150)
  last_name = models.CharField(max_length=150)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  is_superuser = models.BooleanField(default=False)
  date_joined = models.DateTimeField(auto_now_add=True)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):
    return self.email
