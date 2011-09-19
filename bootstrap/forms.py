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
        
class AjaxAutoComplete(forms.Form):
    name = forms.CharField(help_text="Enter a Star Wars character name, e.g Darth",
        label="Star Wars Character",
        widget=forms.TextInput(attrs={'class':'xlarge','help_text' : 'help me'}))