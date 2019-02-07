# -*- coding: utf-8 -*-


from django.contrib import admin
from .models import Profile, User


# Register your models here.



@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=['ID','user','Profile_Type','Name','Added_On','Last_Access','Status','Email']
    list_filter=['Name','City','Address']
