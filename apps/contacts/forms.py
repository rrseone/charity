from django import forms

from apps.contacts.models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'Enter your name',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control valid',
                'placeholder': 'Email'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Select Subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control w-100',
                'placeholder': 'Enter Message'
            }),
        }
