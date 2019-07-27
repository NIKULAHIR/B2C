from django.contrib import admin

# Register your models here.
from .models import Order_details

# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display=['oredr_name']
# admin.site.register(Cart)   
admin.site.register(Order_details)

