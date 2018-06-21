from django import forms
from django.contrib.auth.models import User

from .models import Features


class FeatureForm(forms.ModelForm):
    class Meta:
        model = Features
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'max_length': '100'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'client': forms.Select(attrs={'class': 'form-control'}),
            'priority': forms.TextInput(attrs={'class': 'form-control', 'max_length': '3'}),
            'target_date': forms. DateTimeInput(format='%Y-%m-%d'),
            'product_area': forms.Select(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }


class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}), max_length=150)
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control'}), min_length=8)
