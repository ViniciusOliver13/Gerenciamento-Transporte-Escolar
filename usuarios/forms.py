from django import forms
from django.contrib.auth.forms import AuthenticationForm

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='CPF', widget=forms.TextInput(attrs={'class': 'campo', 'placeholder': 'Seu CPF'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'campo', 'placeholder': 'Sua Senha'}))