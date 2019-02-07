from django.contrib import admin
from .models import (Brand,Item,Category,SubCategory)
# Register your models here.

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(SubCategory)