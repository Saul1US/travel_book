from django import forms
from django.conf import settings
from tinymce.widgets import TinyMCE
from .models import Trip, Place, PlaceImage


class TripForm(forms.ModelForm):
    # title = forms.Textarea()
    class Meta:
        model = Trip
        fields = ('title', )
        # widgets = {
        #     'title': forms.HiddenInput(),
        # }

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
    class Meta:
        model = PlaceImage
        fields = ('images', )
