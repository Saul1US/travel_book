from django import forms
from django.conf import settings
from tinymce.widgets import TinyMCE
from .models import Place, PlaceImage


class PlaceDescriptionForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('content', 'name', 'trip', 'date', 'image' )
        widgets = {
            'content': TinyMCE(), 
            'name': forms.HiddenInput(), 
            'trip': forms.HiddenInput(), 
            'date': forms.HiddenInput(), 
        }

class PlaceImageForm(forms.ModelForm):
    # images=forms.ImageField(label='Upload image')
    class Meta:
        model = PlaceImage
        fields = ('images', )
        # widgets = {
        #     'place': forms.HiddenInput(),
        # }
