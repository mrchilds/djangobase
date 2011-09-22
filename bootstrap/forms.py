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
        widget=forms.TextInput(attrs={'class':'xlarge'}))
        
class PopoverForm(forms.Form):
    popover_input = forms.CharField(label="Form Input Popover",
        widget=forms.TextInput(attrs={'class':'xlarge', 
            'data-content' : 'On focus, this appears - defined in forms.py',
            'data-original-title' : 'My title'}))