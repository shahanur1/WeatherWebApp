from django import forms

# models
from .models import City

class CityForm(forms.ModelForm):

    class Meta:
        model = City
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(
                attrs={
                'class':'form-control'
            }),
        
        }
