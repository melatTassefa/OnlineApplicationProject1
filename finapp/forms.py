
from .models import CustomUser
from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
  
    username = forms.CharField(
        max_length=30,
        help_text='Required. Enter a unique username.',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-3', 'placeholder': 'Enter Username...'})
    )
    email = forms.EmailField(
        max_length=254,
        help_text='Required. Enter a valid email address.',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-3', 'placeholder': 'Email Address'})
    )
    first_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required. Enter your first name.',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-3', 'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        required=True,
        help_text='Required. Enter your last name.',
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-3', 'placeholder': 'Last Name'})
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user mb-3', 'placeholder': 'Password'})
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user mb-3', 'placeholder': 'Confirm Password'})
    )

    role = forms.CharField(
        max_length=100,  # Adjust the max length as per your requirements
        required=True,
        help_text='Enter your role.',  # Provide appropriate help text
        widget=forms.TextInput(attrs={'class': 'form-control form-control-user mb-3', 'placeholder': 'Role'})
    )

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2', 'role')
