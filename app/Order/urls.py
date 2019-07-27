from django.urls import path

from .views import (
                    OrderView, 
                    CartList, 
                    CartDelete,
                    Purches,
                    clear_cart,
                    Confirm_order
                )
urlpatterns=[
    #path('olist/',OrderView.as_view(),name='olist'),

    #product added to cart
    path('olist/<int:pid>/', OrderView.as_view(), name='olist'),
    
    #show the cart list
    path('cartlist/', CartList.as_view(), name='cartlist'),

    #delte or reject cart (cenecel cart product)
    path('cartdel/<int:pid>/', CartDelete.as_view(), name='reject'),

    #buy product
    path('purches/<int:pid>/', Purches.as_view(), name='buy'),

     #clear cart 
    path('clear_cart/', clear_cart.as_view(), name='clear'),

     # confirm Order list 
    path('Confirm_order/',Confirm_order.as_view(),name='Order_confirm'), 

]