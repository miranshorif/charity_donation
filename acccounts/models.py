from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
from .constants import GENDER_CHOICES
# Create your models here.
class User(AbstractBaseUser):
    username        =   None
    email           =   models.EmailField(unique=True, null=False)
    
    objects         =   UserManager()
    
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS =   []
    
    def __str__(self):
        return self.email

class DonationType(models.Model):
    name = models.CharField(max_length=128)
    def __str__(self):
        return self.name    

class Donar(models.Model):
    user            =   models.OneToOneField(User, related_name='donater', on_delete=models.CASCADE)
    account_type    =   models.ForeignKey(DonationType,related_name='accounts',on_delete=models.CASCADE)
    account_no      =   models.IntegerField(unique=True)
    image           =   models.ImageField(upload_to='midea/images')
    gender          =   models.CharField(max_length=7, choices=GENDER_CHOICES)
    date_of_birth   =   models.DateField(null=False)
    
    def __str__(self):
        return str(self.account_no)
    


class DonarAddress(models.Model):
    user                =   models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address      =   models.CharField(max_length=180)
    city                =   models.CharField(max_length=180)
    postal_code         =   models.IntegerField()
    country             =   models.CharField(max_length=180)
    
    def __str__(self):
        return self.user.email