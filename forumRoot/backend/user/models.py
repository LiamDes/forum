from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

#models here.
class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        if username is None:
            raise TypeError('Username required for Users.')
        if email is None:
            raise TypeError('email required for an account.')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self.db)

        return user

    def create_superuser(self, username, email, password):
        # Superuser management
        if password is None:
            raise TypeError('Password required.')
        if email is None:
            raise TypeError('Email required.')
        if username is None:
            raise TypeError('Username required.')
        
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self) -> str:
        return f'{self.email}'