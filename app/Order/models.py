from django.db import models



# Create your models here.


class Order_details(models.Model):

    Profile     =models.ForeignKey(
                                'Profiles.Profile',
                                 on_delete=models.CASCADE,
                                 related_name='Profile',
    )
    Product     =models.ForeignKey(
                                'Product.Item',
                                on_delete=models.CASCADE,
                                related_name='Prod_Details',
    )
    Order_quntity   =models.PositiveIntegerField(
                                default=1,
    )
   

    Order_type  =models.CharField(
                                max_length=5,
                                choices =(
                                        ('SC','Success'),
                                        ('PN','Pending'),
                                        ('RJ','Rejected'),
                                        ('IC','IN Cart'),
                                        ('PR','Processed'),
                                ),
                                default = "PN"
    )  


# class    Order(models.Model):
#     oredr_name  =models.CharField(max_length=100)

#     customer    =models.ForeignKey(
#                                 'Profiles.Profile',
#                                  on_delete=models.CASCADE,
#                                  related_name='Profile',
#     )
#     def __str__(self, *args,**keywrds):
#         return self.oredr_name


# class    Order_details(models.Model):

#     discr       =models.CharField(max_length=100)
#     order       =models.ForeignKey(
#                                     'Order.Order',
#                                     on_delete=models.CASCADE,
#                                     related_name='order_details',
#     )
#     seller      =models.ForeignKey(
#                                     'Product.Item',
#                                     on_delete=models.CASCADE,
#                                     related_name='Produt_details',
#     )
#     def __str__(self, *args,**keywrds):
#         return self.order.oredr_name

# class Cart(models.Model):
#     # Oredr and detials of order needed for cart
#     # using signals cart can be used

#     order       =models.ForeignKey(
#                                     'Order.Order',
#                                     on_delete=models.CASCADE,
#                                     related_name='order',
#     )

