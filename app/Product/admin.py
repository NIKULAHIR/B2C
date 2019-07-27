from django.contrib import admin
from .models import (Brand,Item,Category,SubCategory)
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['Product_Name','Category','Brand','Product_Price','Profile']
    list_filter=['Category','Brand']


admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)