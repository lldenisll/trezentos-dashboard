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

        widgets = {
            'nome':forms.TextInput(attrs={'class':'form-control'}),
            'razaosocial': forms.TextInput(attrs={'class': 'form-control'}),
            'cnpj': forms.TextInput(attrs={'class': 'form-control'}),
            'enderecom': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'})

        }