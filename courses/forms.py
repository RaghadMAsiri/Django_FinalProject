from django import forms 
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm
from .models import Contact



class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ادخل بريدك الالكتروني'})
    )
    
    class Meta:
        model = User
        fields = ["username", "email"]
        
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
        