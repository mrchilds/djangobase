from django import forms
from django.forms import ModelForm

from bootstrap.models import ExampleFields

class ExampleForm(ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'xlarge'}))
    email = forms.CharField(
        widget=forms.TextInput(attrs={'class':'xlarge'}))
    message = forms.CharField(
            widget=forms.Textarea(attrs={'class':'xxlarge'}))    
    class Meta:
        model = ExampleFields