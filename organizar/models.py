from django.db import models
from acccounts.models import Donar
from acccounts.constants import GENDER_CHOICES,BLOOD_GROUP_CHOICES
# Create your models here.
class Organization(models.Model):
    name            =   models.CharField(max_length=100)
    description     =   models.TextField(null=True,blank=False)
    logo            =   models.ImageField(upload_to='midea/organizer')
    email           =   models.EmailField(unique=True)
    
    def __str__(self):
        return self.name
    
class Cause(models.Model):
    name            =   models.CharField(max_length=100)
    description     =   models.TextField(null=False)
    image           =   models.ImageField(upload_to='midea/cause',blank=True)
    
    def __str__(self):
        return self.name
    
class Campaign(models.Model):
    organization    =   models.ForeignKey(Organization, on_delete=models.CASCADE)
    cause           =   models.ForeignKey(Cause, on_delete=models.CASCADE)
    goal_amount     =   models.DecimalField(max_digits=12, decimal_places=2, null=False)
    deadline        =   models.DateField(null=False,blank=False)
    
    
class Donation(models.Model):
    user            =   models.ForeignKey(Donar, on_delete=models.CASCADE)
    organization    =   models.ForeignKey(Organization, on_delete=models.CASCADE)
    donated_to      =   models.ForeignKey(Campaign, on_delete=models.CASCADE)
    amount          =   models.DecimalField(max_digits=12, decimal_places=2)
    donated_at      =   models.DateTimeField(auto_now_add=True) 
    
