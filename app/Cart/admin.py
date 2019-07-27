from django.contrib import admin
from .models import MyCart
# Register your models here.


@admin.register(MyCart)
class MyCartAdmin(admin.ModelAdmin):
    pass