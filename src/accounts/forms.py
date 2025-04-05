from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Addresse e-mail", widget=forms.EmailInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:ring-2 focus:ring-blue-500 focus:outline-none'
        }))
    fullname = forms.CharField(max_length=120, min_length=5, required=True, label="Nom Prénom", widget=forms.TextInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:ring-2 focus:ring-blue-500 focus:outline-none'
        }))
    password1 = forms.CharField(required=True, label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )
    password2 = forms.CharField(required=True, label="Confirmer votre mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:ring-2 focus:ring-blue-500 focus:outline-none'
        })
    )

    class Meta:
        model = User
        fields = ["email", "fullname"]

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(required=True, label="Addresse e-mail", widget=forms.EmailInput(attrs={
            'class': 'border border-gray-300 rounded-lg p-2 w-full focus:ring-2 focus:ring-blue-500 focus:outline-none'
        }))
    password = forms.CharField(required=True, label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'border border-gray-300 rounded-lg p-2 w-full focus:ring-2 focus:ring-blue-500 focus:outline-none'
                                })
                                )
