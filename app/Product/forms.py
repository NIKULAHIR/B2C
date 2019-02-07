from django import forms
from .models import Item
from django.contrib.auth.models import User

class AddProductForm(forms.ModelForm):
    #Profile = forms.CharField(disabled=True)
    #Product_Image =forms.CharField(disabled=True)      
    #disabled_fields =('Profile')       #-----//what shoud we can do with foreignkey???
   
    class Meta:
        model = Item
        exclude = []
    #     widgets = {
    #     'Profile': forms.TextInput(attrs={'disabled': True}),
    # }

    # def __init__(self, *args, **kwargs):
    #     super(AddProductForm, self).__init__(*args, **kwargs)
    #     for x in self.disabled_fields:
    #         self.fields[x].disabled = True

    # def __init__(self, *args, **kwargs):
    #     super(AddProductForm, self).__init__(*args, **kwargs)
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.pk:
    #         self.fields[instance].disabled = True

            
    # def clean_Profile(self):
    #     instance = getattr(self, 'instance', None)
    #     if instance and instance.id:
    #         return instance.Profile
    #     else:
    #         return self.cleaned_data['Profile']