from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

class UserManager(BaseUserManager):

  def create_user(self, username, email, password=None, **kwarg):
    if email is None:
      raise TypeError("Users must have an email.")

    user = self.model(username=username, email=self.normalize_email(email))
    user.set_password(password)
    user.save(using=self._db)

    return user
  
  def create_superuser(self, username, email, password):
    user = self.create_user(username, email, password)
    user.is_superuser = True
    user.is_staff = True
    
    user.save(using=self._db)

    return user
 
class User(AbstractBaseUser, PermissionsMixin):
  username = models.CharField("username", max_length=240)
  description = models.TextField(max_length=3000)
  email = models.EmailField(unique=True)
  phone = models.CharField(max_length=20)
  date_joined = models.DateTimeField(auto_now_add=True)
  last_login = models.DateTimeField(null=True)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)
  updated = models.DateField(auto_now=True)

  USERNAME_FIELD = 'email'

  objects = UserManager()

  def set_description(self, description):
    self.description = description
  
  def set_phone(self, phone_number):
    self.phone = phone_number

  def set_email(self, email):
    self.email = email
  
  def set_username(self, username):
    self.username = username

  def __str__(self):
    return f"{self.email}"

