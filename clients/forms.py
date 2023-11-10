from django import forms 
from . models import Newsletter, Contact_us_Message, IntrestedClient, Invoice

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = IntrestedClient
        fields = ('name', 'business_name', 'phone', 'email', 'location', 'refferal_code', 'username', 'password')

        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'business_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Business Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Phone Number'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Business Location'
            }),
            'refferal_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your refferal code'
            }),
            'username': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Your Username'
            }),
            'password': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'your pasword'
            })
        }

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = Contact_us_Message
        fields = ('name', 'email', 'subject', 'message')

        widgets ={
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            }),
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Subject'
            }),
            'name': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Message'
            })
        }

class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = ('email',)

        widgets ={
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Your Email'
            })
        }

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ('payment_code',)

        widgets ={
            'payment_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Payment Reffrence Code'
            })
        }
