from django.db import models

# Create your models here.

#lets build the user model manager

from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _

#usermodel imports
from django.contrib.auth.models import AbstractBaseUser, AbstractUser, PermissionsMixin
from django.utils import timezone


from rest_framework_simplejwt.tokens import RefreshToken

class CustomUserManager(BaseUserManager):
    # custom user model manager where email is the unique identifiers
    # for authentication instead of usernames
    
    def create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError(_('The Email must be set'))
        email= self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        password=password
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email,password,**extra_fields):

        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        extra_fields.setdefault('is_active',True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError (_('Superuser must have is_staff=True'))

        if extra_fields.get('is_superuser') is not True:
            raise ValueError (_('Superuser must have is_superuser=True'))

        if extra_fields.get('is_active') is not True:
            raise ValueError (_('Superuser must have is_active=True'))

        user = self.create_user(email,password, **extra_fields)
        user.save()
        return user



#i have the option of using Abstractuser if i want to keep django default fields
#else like in this case i would use Abstractbase user

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email =  models.EmailField(max_length=254, unique=True, db_index=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    # email_verification = models.BooleanField(default=False)
    username =  models.CharField(max_length=254, unique=True, db_index=True,null=True,blank=True)
    first_name = models.CharField(max_length=254)
    last_name = models.CharField(max_length=254)
    created_at=models.DateTimeField(auto_now_add=True)
    link = models.CharField(max_length=254,default='null')
    location = models.CharField(max_length=254)
    bio = models.CharField(max_length=254)
    skills = models.CharField(max_length=254)
    profile_pics = models.ImageField(upload_to='upload')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects=CustomUserManager()
    
    def __str__(self):
        return self.email

    # def tokens(self):
    #
    #     refresh=RefreshToken.for_user(self)
    #     return {
    #         "refresh":str(refresh) ,
    #         "access": str(refresh.access_token)
    #     }







# #project models
# class Projects (models.Model):
#     image=models.ImageField(upload_to='upload')
#     title=models.CharField(max_length=254)
#     desc=models.CharField(max_length=254)
#     roles=models.CharField(max_length=254)
#     tools=models.CharField(max_length=254)
#     comp=models.CharField(max_length=254)
#     data=models.CharField(max_length=254)




