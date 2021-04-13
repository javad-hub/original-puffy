from django import forms
from . import models

class CreateShit(forms.ModelForm):
    class Meta:
        model = models.Shit
        fields = ['title', 'slug','body','image']
