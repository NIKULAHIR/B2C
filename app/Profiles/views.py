from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User   
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Profile
from .forms import LoginForm, RegisterForm, ProfileForm
from django import views



class LoginView(views.View):
    def get(self, request, *args, **keywrds):
        return render(
             request,
            'login.html',
             context={
                'form' : LoginForm()
            }
        )
    def post(self,request,*args,**keywrds):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password'],
            )
            if user:
                login(request, user)
                return redirect('root:profile')
            else:
                #form.add_error('username','Inavlid username')
                return render(
                    request,
                    'login.html',
                    context={
                        'form':LoginForm(),
                        "error":"Invalid username and password name",
                    }
                )
        else:
            return render(
                request,
                'login.html',
                context={
                    'form' : form
                }
            )
def LogoutView(request):
    logout(request)
    return redirect('root:login') 

class RegisterView(views.View):
    def get(self, request, *args, **keywrds):
        return render(
            request,
            'register.html',
            context={
                'form' : RegisterForm()
            }
        )
    def post(self, request, *args, **keywrds):
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                username = form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
            )
            Profile.objects.create(
                user = user
            )
            login(request, user)
            return redirect('root:profile')
        else: 
            return render(
                request,
                'register.html',
                context={
                    'form' : form
                }
            )
class ProfileView(LoginRequiredMixin,views.View):
    login_url = "/profile/login/"
    

    def get(self, request, cid = None, *args, **kwargs):

        #this will ridirect tocustomerwhile Profile type is Customer
        if request.user.Profile.Profile_Type == 'CS':
            return redirect('product:cat_list')
            # return HttpResponse(
            #     #status=400,
            #     """<h1>The user is not--> Seller,</h1>
            #     <h3>Page Redirect to the Customer View</h3>"""
            # )  

        if not cid:
            return render(
                request,
                'profile.html',
                #'index.html',
                context={
                    'form' : ProfileForm(
                        instance=request.user.Profile
                    )
                }
            )
        else: 
            try:
                return render(
                    request,
                    'profile.html',
                    #'index.html',
                    context={
                        'form' : ProfileForm(
                            instance=Profile.objects.get( id = cid )
                        )
                    }
                )
            except Exception as e:
                return HttpResponse(
                    status = 404
                )
    def post(self, request, cid = None, *args, **kwargs):
        if cid:
            try:
                profile = Profile.objects.get(id = cid)
            except Exception as e :
                return HttpResponse(
                    status = 404
                )
        else:
            profile = request.user.Profile
        
        form = ProfileForm(
            instance=profile,
            data=request.POST,
        )
        if form.is_valid():
            form.save()
            #form.create()
            return render(
                request,
                'profile.html',
                context={
                    'form' : form,
                    "errors" : "Profile Updated Sucessfully",
                }
            )
        else:
            return render(
                request,
                'profile.html',
                context={
                    'form' : form,
                }
            )

        