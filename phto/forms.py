from django import forms
from .models import Phto

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Phto
        fields = (
            'title',
            'author',
            'image',
            'description',
            'price',
        )