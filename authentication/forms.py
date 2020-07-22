# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder" : "Email",                
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password check",                
                "class": "form-control"
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class ProfileForm(forms.ModelForm):
    nomeCliente = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nome do Cliente",
                "class": "form-control"
            }
        ))
    pontoFocalCliente = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Ponto focal do Cliente",
                "class": "form-control"
            }
        ))
    dataIncio = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Data de início da obra",
                "class": "form-control"
            }
        ))
    dataFim = forms.DateField(
        widget=forms.DateInput(
            attrs={
                "placeholder": "Data de término da obra",
                "class": "form-control"
            }
        ))
    gerenteContrato = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Gerente do contrato",
                "class": "form-control"
            }
        ))
    enderecoObra = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Endereço da obra",
                "class": "form-control"
            }
        ))
    cidadeObra = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Cidade da obra",
                "class": "form-control"
            }
        ))
    estadoObra = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Estado da obra",
                "class": "form-control"
            }
        ))
    cepObra = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "CEP",
                "class": "form-control"
            }
        ))
    infoGeral = forms.CharField(
        widget=forms.Textarea(
            attrs={
                "placeholder": "Informações gerais da obra",
                "class": "form-control"
            }
        ))

    class Meta:
        model = Profile
        fields = ('nomeCliente','pontoFocalCliente', 'dataIncio',
                  'dataFim','gerenteContrato','enderecoObra',
                  'cidadeObra', 'estadoObra', 'cepObra', 'infoGeral')
