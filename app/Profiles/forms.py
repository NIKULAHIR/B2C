from django import forms
from django.contrib.auth.models import User

from .models import(Profile)

class LoginForm(forms.Form):
    username =forms.CharField(
        label='User Name :',
        max_length=150,
    )
    password    =forms.CharField(
        label='Password :',
        max_length=16,
        widget=forms.PasswordInput(),
    )
    def clean_username(self, *args, **keywrds):
        try:
            User.objects.get(username=self.cleaned_data['username'])
            return self.cleaned_data['username']
        except forms.ValidationError as e:
            raise forms.ValidationError("User not Found!")
        except Exception as e:
            raise forms.ValidationError("Register you Email!")

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        exclude = ['Birthdate','BillingAddress','ShippingAddress']

        def __init__(self, *args, **kwargs):
            disabled_fields = ('Profile')
            super(ProfileForm, self).__init__(*args, **kwargs)
            for x in self.disabled_fields:
                self.fields[x].disabled = True
    #     widgets = {
    #     'user': forms.TextInput(attrs={'disabled': True}),
    # }


class RegisterForm(forms.Form):
    username    =forms.CharField(
        label='User Name :',
        max_length=150,
    )
    email       =forms.EmailField(
        label='Ypur Email :',
    )
    password1=forms.CharField(
        label='Password :',
        widget=forms.PasswordInput(),
        max_length=20,
    )
    password2=forms.CharField(
        label='ConfirmPassword :',
        widget=forms.PasswordInput(),
        max_length=20,
    )
    def clean_username(self,*args,**keywrds):
        try:
            User.objects.get(username = self.cleaned_data['username'])
            raise forms.ValidationError('User alrady exist!')
        except forms.ValidationError as e:
            raise forms.ValidationError('User alredy exist!!!!')
        except Exception as e:
            return self.cleaned_data['username']

    def clean_password1(self,*args,**keywrds):
        if self.data['password1'] == "" or self.data['password2'] == "":
            raise forms.ValidationError("Password Can not be blank")
        if self.data['password1'] != self.data['password2']:
            raise forms.ValidationError("Password Does not Match")
        else:
            return self.cleaned_data['password1']