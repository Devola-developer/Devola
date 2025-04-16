from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your name',
                'id': 'name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'example@mail.com',
                'id': 'email'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message here...',
                'rows': 5,
                'id': 'message'
            }),
        }
        labels = {
            'name': 'Name:',
            'email': 'E-mail address:',
            'message': 'Message:',
        }
