from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Addresse e-mail", widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }))
    fullname = forms.CharField(max_length=120, min_length=5, required=True, label="Nom Prénom", widget=forms.TextInput(attrs={
            'class': 'form-control'
        }))
    password1 = forms.CharField(required=True, label="Mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )
    password2 = forms.CharField(required=True, label="Confirmer votre mot de passe",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = User
        fields = ["email", "fullname"]

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.EmailField(required=True, label="Addresse e-mail", widget=forms.EmailInput(attrs={
            'class': 'form-control'
        }))
    password = forms.CharField(required=True, label="Mot de passe", widget=forms.PasswordInput(attrs={'class': 'form-control'
                                })
                                )
