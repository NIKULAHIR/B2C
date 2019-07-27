from django.urls import path
from .views import (
    ProductListView,
    DeleteProductView,
    AddProductView,
    EditProductView,
    CategoryListView,
    BrandListView,
    ProductList,#user view,
    SubCategoryListView,
    Pending_order,
    #Confirm_order,
)
urlpatterns=[
    #Product List s for seller
    path('prod_list/',ProductListView.as_view(),name='list'),
    
    #product list for customer(user)
    path('p_list/<int:catid>/',ProductList,name='p_list'),
    #category list
    path('cat_list/', CategoryListView.as_view(), name='cat_list'),
    path('sub_cat/<int:catid>/', SubCategoryListView.as_view(), name='sub_cat'),
   
    #Brand list
    path('brand_list/', BrandListView.as_view(), name='brand_list'),

    #Add Product
    #path('list/<int:cid>/details',ProductListView.as_view() , name='list'),
    path('add_product/',AddProductView.as_view(),name='add_product'),
    path('add_product/<int:pid>',AddProductView.as_view(),name='add_product'),

    #delete Product
    #path('delete/',DeleteProductView.as_view(), name='delete'),
    path('delete/<int:pid>/',DeleteProductView.as_view(), name='delete'),

    #Edit Product
    #path('edit_product/',EditProductView.as_view(),name='edit_product'),
    path('edit_product/<int:pid>/',EditProductView.as_view(),name='edit_product'),


    #Order list 
    path('Order_pending/',Pending_order.as_view(),name='Order_list'),

    # confirm Order list 
    #path('Confirm_order/',Confirm_order.as_view(),name='Order_confirm'), 

    
]