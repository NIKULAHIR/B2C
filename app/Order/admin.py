from django.contrib import admin

# Register your models here.
from .models import Order, Order_details, Cart

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=['oredr_name']
    
admin.site.register(Order_details)
admin.site.register(Cart)
