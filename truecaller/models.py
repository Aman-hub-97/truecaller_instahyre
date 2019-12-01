from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import PermissionsMixin
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self,name,contact,email,password=None):
        
        user= self.model(name=name,contact=contact,email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user

    
    def create_superuser(self,name,contact,password=None):

        user= self.model(name=name,contact=contact)
        user.set_password(password)
        user.is_superuser= True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser,PermissionsMixin):
    name= models.CharField(max_length=50,null=False,unique=True)
    contact= models.CharField(max_length=12,null=True,unique=True)
    email= models.EmailField(max_length=50,unique=True,null=True)
    spam= models.BooleanField(default=False)
    active= models.BooleanField(default=True)
    
    
    
    objects= UserManager()
    USERNAME_FIELD='name'
    REQUIRED_FIELDS=['contact']

        
    def __str__(self):
        return self.name


class ProfileMapping(models.Model):

    user= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    contact= models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='contact_set'
    )
    status= models.BooleanField(default=True)
    created_on= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.status_text