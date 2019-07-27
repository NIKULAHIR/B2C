from django.db import models
#from django.contrib.auth.models import User
#from django.db import models

from django.utils import timezone
#from django.core.validators import MaxValueValidator, MinValuehValidator
# Create your models here.

class Item(models.Model):
    #user            =models.OneToOneField(User,on_delete=models.CASCADE,related_name="profile")
    Profile      =models.ForeignKey(
                                    'Profiles.Profile',
                                    #.choices["SL"]'
                                    #/.Seller/.choices[1]',
                                    on_delete=models.CASCADE,
                                    related_name='seller_Product',
                                )
    Brand        =models.ForeignKey(
                                    'Product.Brand',
                                    on_delete=models.CASCADE,
                                    related_name='Product_Brand',
                                )
    Category     =models.ForeignKey(
                                    'Product.Category',
                                    on_delete=models.CASCADE,
                                    related_name='product_category',
                                )
   
    Product_Name  =models.CharField(
                                        max_length=50
                                    )
    Product_Price =models.IntegerField(
                                default=100,
                                # validators=[
                                #     MinValueValidator(5),
                                #     MaxValueValidator(10),
                                # ]
                                )
    Product_Image =models.CharField(                #-----Use-Image Field
                                        max_length=30,  
                                        default='unknown'
                                    )
    def __str__(self,*args,**kywords):
        return self.Product_Name


class Brand(models.Model):
    Brand_Name    =models.CharField(
                                    max_length=50
                                )
    def __str__(self,*args,**kywords):
        return self.Brand_Name

class Category(models.Model):
    
    Category_Name=models.CharField(
                                    max_length=50,
                                    choices=(
                                            ('CL','Cloth'),
                                            ('FT','Footware'),
                                            ('MP','Mobile Phone'),
                                            ('Lp','Laptop'),
                                    ),
                                )
    
    def __str__(self,*args,**kywords):
        return self.Category_Name
    

class SubCategory(models.Model):
    Category     =models.ForeignKey(
                                        'Product.Category',
                                        on_delete=models.CASCADE,
                                        related_name='Sub_Category',
                                    )
    
    
    SubCatName  =models.CharField(

                                    max_length=50,
                                    choices=(
                                            ('MN','Men'),
                                            ('WM','Women'),
                                            ('CH','Child'),
                                            ('SH','Shoes'),
                                            ('SD','Shandal'),
                                            ('SL','Sleeper'),
                                            ('SM','Smart Phone'),
                                            ('SP','Sale phone'),
                                            ('TB','Tablate'),
                                    ),
                                
    )
    
    def __str__(self,*args,**kywords):
        return self.SubCatName
    

# Create your models here.
# class Product(models.Model):
#     pass

# class Product_details(models.Model):
#     pass

# class Brand(models.Model):
#     pass

# class Cetegory(models.Model):
#     pass

# class Sub_Cetegory(models.Model):
#    pass