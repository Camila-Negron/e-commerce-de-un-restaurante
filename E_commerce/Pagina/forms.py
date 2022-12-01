from django import forms

from .models import Administrador

class LoginForm(forms.Form):
    user = forms.CharField(widget=forms.TextInput(attrs={
        "type":"text",
        "name": "user",
        "placeholder": "Usuario"
    }))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        "type":"password",
        "name": "pass",
        "placeholder": "Constraseña"
    }))