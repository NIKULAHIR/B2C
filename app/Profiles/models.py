
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

from django.db.models.signals import post_save


class Profile(models.Model):
    user            =models.OneToOneField(User,on_delete=models.CASCADE,related_name="Profile")
    Profile_Type    =models.CharField(
                                        max_length=2,   
                                        choices=(
                                            ('CS','Customer'),
                                            ('SL','Seller'),
                                            ('AD','Admin'),
                                        ),
    )  
    Name            =models.CharField(max_length=50)
    State           =models.CharField(max_length=50)
    City            =models.CharField(max_length=50)
    Address         =models.TextField()
    Birthdate       =models.DateField(default=timezone.now)
    Contact_No      =models.IntegerField(blank=True, null=True)
    Status          =models.BooleanField(default=True)
    Email           =models.EmailField()
    Added_On        =models.DateTimeField(auto_now_add=True)
    Last_Access     =models.DateTimeField(auto_now=True)
    BillingAddress  =models.CharField(max_length=100)
    ShippingAddress =models.CharField(max_length=100)
    Logo            =models.CharField(max_length=5)

    def __str__(self,*args,**keywrds):
        return self.user.username

    # def Create_Profile(self, sender, *args, **keywrgs):
    #     user    = keywrgs['instance']
    #     if keywrgs['created']:
    #         profile = user.models.Profile()
    #         profile.setUser(sender)
    #         profile.save()
    # post_save.connect(Create_Profile, sender=User)