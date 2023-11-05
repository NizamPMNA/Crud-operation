from django import forms
from django.forms import ModelForm
from . models import LanguageInfo

class LanguageForm(ModelForm):
    class Meta:
        model = LanguageInfo
        fields = '__all__'
        
    # Apply CSS classes to form fields and labels
        widgets = {
            'language': forms.TextInput(attrs={'class': 'input-class'}),
            'designed_by': forms.TextInput(attrs={'class': 'input-class'}),
            'developer': forms.TextInput(attrs={'class': 'input-class'}),
            'os': forms.TextInput(attrs={'class': 'input-class'}),
            'year': forms.NumberInput(attrs={'class': 'input-class'}),
            'description': forms.Textarea(attrs={'class': 'input-class'}),
        }

        labels = {
            'language': 'Language',
        }
        
