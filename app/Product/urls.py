from django.urls import path
from .views import (
    ProductListView, 
    DeleteProductView,
    AddProductView,
    EditProductView,
)
urlpatterns=[
    
    path('list/',ProductListView.as_view(),name='list'),
    #path('list/<int:cid>/details',ProductListView.as_view() , name='list'),
    path('add_product/',AddProductView.as_view(),name='add_product'),
    path('add_product/<int:pid>',AddProductView.as_view(),name='add_product'),
    #path('delete/',DeleteProductView.as_view(), name='delete'),
    path('delete/<int:pid>/',DeleteProductView.as_view(), name='delete'),

    #path('edit_product/',EditProductView.as_view(),name='edit_product'),
    path('edit_product/<int:pid>/',EditProductView.as_view(),name='edit_product'),
]