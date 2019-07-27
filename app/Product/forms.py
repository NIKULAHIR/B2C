from django import forms
from .models import Item
from django.contrib.auth.models import User

class AddProductForm(forms.ModelForm):

    class Meta:
        model = Item
        exclude = []
        widgets = {
            'Profile': forms.HiddenInput(),
        }

    #Profile = forms.CharField(disabled=True)
    #Product_Image =forms.CharField(disabled=True)
    #disabled_fields =('Profile')       #-----//what shoud we can do with foreignkey???

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.fields['Profile'].widgets = forms.HiddenInput()

class EditPrdoductForm(forms.ModelForm):
    class Meta:
        model= Item
        exclude=[]
        widgets = {
            'Profile': forms.HiddenInput(),
        }
    def __init__(self, *args, **kwargs):
        super(EditPrdoductForm, self).__init__(*args, **kwargs)
        # self.fields['Profile'].disabled = True

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