from django.db import models

#from django.db import models

from django.utils import timezone
#from django.core.validators import MaxValueValidator, MinValuehValidator
# Create your models here.

class Item(models.Model):
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
    Product_Image =models.CharField(
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
                                    max_length=50
                                )
    Sub_Category     =models.ForeignKey(
                                        'Product.SubCategory',
                                        on_delete=models.CASCADE,
                                        related_name='Sub_Category',
                                    )
    def __str__(self,*args,**kywords):
        return self.Category_Name
    

class SubCategory(models.Model):
    
    
    SubCatName  =models.CharField(max_length=50)
    
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