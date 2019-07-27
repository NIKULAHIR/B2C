from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
# from Profile.models import Profile
from .models import  Order_details
from django import views
# # Create your views here.
# from .forms import (OrderForm,
#                     Order_detailsForm, 
#                     CartForm)


from app.Product.models import Item

class OrderView(LoginRequiredMixin, views.View):
    login_url="/profile/login/"

    def get(self,request,pid, *args, **keywrgs):
        product = Item.objects.get(id=pid)
        Order_details.objects.create(
            Profile = request.user.Profile,
            Product = product,
        )

        #return render("product succesfully added to cart")


        return render(
                        request,
                        'added.html',
                        context={
                            "msg":"Product aaded succesfully to cat"
                        }
        )

class CartList(LoginRequiredMixin,views.View):
    login_url="/profile/login/"

    def get(self,request, *args,**keywrds):
       
        
        return render(
            request,
            'ol.html',
            context={
                    'odl':Order_details.objects.filter(Profile = request.user.Profile, Order_type="PN"),
                    'cart_count' : Order_details.objects.filter(Profile = request.user.Profile, Order_type="PN").count(),
  
                
                }
            )

class clear_cart(LoginRequiredMixin,views.View):
    login_url="/profile/login/"

    def get(self,request, *args,**keywrds):
       
        
        return render(
            request,
            'ol.html',
            context={
                    
                    'cart_count' : Order_details.objects.filter(Profile = request.user.Profile, Order_type="PN").delete(),
  
                
                }
            )

class CartDelete(LoginRequiredMixin, views.View):
    login_url="/profile/login/"


    def get(self, request, pid,*args,**keywrgd):
        
        # if request.user.Profile.Profile_Type != 'SL':
        #     return HttpResponse(
        #         #status=400,
        #         "The user is not--> Seller"
        #     )   
        Order_details.objects.get(id=pid).delete()
        
        return redirect('order:cartlist')



    # # def post(self, *args, **keywrgs):
    #     pass

class Purches(LoginRequiredMixin, views.View):
    login_url="/profile/login/"


    def get(self, request, pid,*args,**keywrgd):
        
        # if request.user.Profile.Profile_Type != 'SL':
        #     return HttpResponse(
        #         #status=400,
        #         "The user is not--> Seller"
        #     )   
        
        
        return HttpResponse("Order places succesfully...\nWait for confirmation")

class Confirm_order(LoginRequiredMixin, views.View):
    login_url="/profile/login/"

    def get(self,request,pid, *args, **keywrgs):
        if request.user.Profile.Profile_Type != 'SL':
            product = Item.objects.get(id=pid)
            Order_details.objects.create(
                Profile = request.user.Profile,
                Product = product,
                Order_type="SC"
            )

            #return render("product succesfully added to cart")


            return render(
                            request,
                            'confirm.html',
                            context={
                                "msg":"order confirm succesfully "
                            }
            )