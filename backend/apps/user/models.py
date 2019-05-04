from __future__ import unicode_literals
from django.db import models
from backend.functions.make_id import *
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

class User(AbstractBaseUser, PermissionsMixin):
    cr_id = create_id
    id = models.CharField(default= cr_id(), primary_key=True, max_length=255) 
    username = models.CharField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password']
    is_anonymous = False
    is_authenticated = True
    objects = UserManager()
    def _str_(self):
        return self.username, self.name, self.id
