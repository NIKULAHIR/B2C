from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User
class MyCart(models.Model):
    """
    prodid-FK
    userid-FK
    quantity
    totale_price
    created
    modified
    """
    Product         =models.ForeignKey(
                        "Product.Item",
                        on_delete = models.CASCADE,
                        related_name="prodID",
    )
    Profile         =models.ForeignKey(
                        "Profiles.Profile",#User.Customer
                        on_delete = models.CASCADE,
                        related_name = "UserID",
    )
    quantity        =models.IntegerField(default=0)


    created         =models.DateTimeField(auto_now_add = True)
    modified        =models.DateTimeField(auto_now = True)
    totale_price    =models.IntegerField(default=0)
    image           =models.CharField(max_length=30)    #Use----ImageField

    def __str__(self, *args, **keywrgs):
        return self.image

   