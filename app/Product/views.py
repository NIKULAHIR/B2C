from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
#from Profile.models import Profile
from .models import Item
from django import views

from .forms import (
    AddProductForm,
)
# Create your views here.

class ProductListView(LoginRequiredMixin,views.View):
    login_url="/profile/login/"

    def get(self,request,*args,**keywrds):
        if request.user.Profile.Profile_Type != 'SL':
            return HttpResponse(
                #status=400,
                """The user is not--> Seller,
                can't see the product list"""
                

            )
            

        context={'pl':Item.objects.all()}
        return render(request,'lop.html',context)
                                # 'pl',Product.Item.objects.all()
        # try:
        # except Exception as e:
        #     return HttpResponse('page not found')



class AddProductView(LoginRequiredMixin,views.View):
    login_url="/profile/login/"

    def get(self, request,pid=None, *args, **keywrgs):

        if request.user.Profile.Profile_Type != 'SL':
            return HttpResponse(
                #status=400,
                "The user is not--> Seller"

            )
            
        if not pid:
            return render(
                            request,
                            'demo.html',
                            context={
                                'form':AddProductForm(
                                 #instance= request.user.Item.seller_Product
                            )
                        }
                    )
        else:
            return render(
                            request,
                            'lop.html',
                            context={
                                'form':AddProductForm(
                                   instance=Item.objects.get(id = pid)
                            )
                        }
                    )  
    def post(self, request,pid=None, *args, **keywrgs):
        
       

        form = AddProductForm(
                
                data=request.POST,
            )

        if form.is_valid():
            form.save()     #form.create()
            return render(
                    request,
                    'demo.html',
                    context={
                        'form' : form,
                        "errors" : "Profile Updated Sucessfully",
                    }
                )
        else:
            return render(
                    request,
                    'demo.html',
                    context={
                        'form' : form,
                    }
            )


class DeleteProductView(LoginRequiredMixin, views.View):

    login_url="/profile/login/"


    def get(self, request, pid=None,*args,**keywrgd):
        # quer=Item.objects.filter(id=pid)
        # quer.delete()

        Item.objects.get(id=pid).delete()
        
        return redirect('product:list')


class EditProductView(LoginRequiredMixin, views.View):

    def get(self, request,pid, *args, **keywrgs):
        if request.user.Profile.Profile_Type != 'SL':
            return redirect('product:list')
            
        # if not pid:
        #     return HttpResponse(
        #         status=400
        #     )
        else: 
            try:
                return render(
                    request,
                    'demo.html',
                    context={
                        'form' : AddProductForm(
                            instance=Item.objects.get( id = pid )
                        )
                    }
                )
            except Exception as e:
                return HttpResponse(
                    status = 404
                )
    
    def post(self, request, pid,*args, **keywrgs):
        if request.user.Profile.Profile_Type != 'SL':
            return HttpResponse(
                #status=400,
                "The user is not--> Seller"

            )
        if pid:
            try:
                seller_Product = Item.objects.get(id = pid)
            except Exception as e :
                return HttpResponse(
                    status = 404
                )
        else:
            
            return HttpResponse(
                status=404
            )
           
        
        form = AddProductForm(
            instance=seller_Product,
            data=request.POST,
        )
        if form.is_valid():
            form.save()
            return render(
                request,
                'demo.html',
                context={
                    'form' : form,
                    "errors" : "Profile Updated Sucessfully",
                }
            )
        else:
            return render(
                request,
                'demo.html',
                context={
                    'form' : form,
                }
            )
