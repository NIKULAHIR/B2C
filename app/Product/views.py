from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, authenticate
from app.Profiles.models import Profile
from .models import Item, Category, Brand, SubCategory
from django import views
from app.Order.models import Order_details
from .forms import (
    #LoginForm,
    AddProductForm,
    EditPrdoductForm,
)
# Create your views here.

class ProductListView(LoginRequiredMixin,views.View):
    login_url="/profile/login/"

    def get(self,request,*args,**keywrds):
        # if request.user.Profile.Profile_Type != 'SL':
        #     return HttpResponse(
        #         #status=400,
        #         "The user is not--> Seller"
        #     )   
        context={'pl':Item.objects.all()}
        return render(request,'lop.html',context)


 
                                # 'pl',Product.Item.objects.all()

def ProductList( request, catid = None):
    if catid is not None:
        context={'pl':Item.objects.filter( Category__Sub_Category__id = catid )}
        return render(request,'p_list.html',context)

    else:
        context={'pl':Item.objects.all()}
        return render(request,'p_list.html',context)


class CategoryListView(views.View):
    login_url="/profile/login/"

    def get(self,request, *args, **keywrgs):

       
   
    
        return render(
                        request,
                        'catg.html',
                        context = {
                            'cl':Category.objects.all()#(Category_Name__startswith=''),
                            
                        }
            )
class SubCategoryListView(views.View):
    #login_url="/profile/login/"

    def get(self,request, catid,*args, **keywrgs):

            return render(
                        request,
                        'sub_cat.html',
                        context = {
                            'cl':Category.objects.get(pk = catid).Sub_Category.all() #(Category_Name__startswith=''), 
                        }
            )
class BrandListView(LoginRequiredMixin, views.View):
    login_url="/profile/login/"

    def get(self,request, *args, **keywrgs):

        return render(
                    request,
                    'bdl.html',
                    context = {
                        'bd':Brand.objects.filter(),
                        
                    }
        )

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
                            'addprod.html',
                            context={
                                'form':AddProductForm(
                                    #instance=Item.objects.get( id = pid ),
                                    initial = {
                                        "Profile" : request.user.Profile,
                                    }
                                
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
                    'addprod.html',
                    context={
                        'form' : form,
                        "errors" : "Profile Updated Sucessfully",
                    }
                )
        else:
            return render(
                    request,
                    'addprod.html',
                    context={
                        'form' : form,
                    }
            )


class DeleteProductView(LoginRequiredMixin, views.View):

    login_url="/profile/login/"


    def get(self, request, pid=None,*args,**keywrgd):
        # quer=Item.objects.filter(id=pid)
        # quer.delete()
        if request.user.Profile.Profile_Type != 'SL':
            return HttpResponse(
                #status=400,
                "The user is not--> Seller"
            )   
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
                    'addprod.html',
                    context={
                        'form' : EditPrdoductForm(
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
           
        
        form = EditPrdoductForm(
            instance=seller_Product,
            data=request.POST,
        )
        if form.is_valid():
            form.save()
            return render(
                request,
                'addprod.html',
                context={
                    'form' : form,
                    "errors" : "Profile Updated Sucessfully",
                }
            )
        else:
            return render(
                request,
                'addprod.html',
                context={
                    'form' : form,
                }
            )

class Pending_order(LoginRequiredMixin,views.View):
    login_url="/profile/login/"

    def get(self,request,*args,**keywrds):
        # if request.user.Profile.Profile_Type != 'SL':
        #     return HttpResponse(
        #         #status=400,
        #         "The user is not--> Seller"
        #     )   
        context={'order':Order_details.objects.all()}
        return render(request,'cifodr.html',context)


# class Confirm_order(LoginRequiredMixin,views.View):
#     login_url="/profile/login/"

#     def get(self,request,*args,**keywrds):
#         if request.user.Profile.Profile_Type != 'SL':
#             return HttpResponse(
#                 #status=400,
#                 "The user is not--> Seller"
#             )   
#         context={'cnf':Order_details.objects.filter(Order_type="SC")}
#         return render(request,'cifodr.html',context)


 