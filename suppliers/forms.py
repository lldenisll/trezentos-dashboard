from django import forms
from .models import Suppliers

class SuppliersForm(forms.ModelForm):
    class Meta:
        model = Suppliers
        fields = {
            'nome':'nome',
            'razaosocial':'Razão Social',
            'cnpj': 'cnpj',
            'enderecom':'Endereço',
            'telefone': 'Tel()'
        }

        labels = {
            'nome': 'Nome do fornecedor',
            'razaosocial': 'Razão Social',
            'cnpj': 'CNPJ',
            'enderecom': 'Endereço',
            'telefone': 'Telefone para contato com DDD'
        }

        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'razaosocial': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'enderecom': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'})

        }