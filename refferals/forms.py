from django import forms 
from . models import Refferal
from django.contrib.auth.forms import  AuthenticationForm

class SalesRepForm(forms.ModelForm):
    class Meta:
        model = Refferal
        fields = ('name', 'username', 'phone', 'location')

        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'username': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your username Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Location'
            })
        }


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : '',
        'class': 'form-control rounded-xl'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : '',
        'class': 'form-control rounded-xl'
    }))