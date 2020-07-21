from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields =  {

            'nomeCliente' : 'Nome do cliente',
            'pontoFocalCliente': 'Ponto focal do cliente',
            'dataIncio': 'Data de início da Obra',
            'dataFim' : 'Data prevista para o fim da obra',
            'gerenteContrato':'Gerente do contrato',
            'enderecoObra' : 'Endereço da obra',
            'cidadeObra' : 'Cidade',
            'estadoObra' : 'Estado',
            'cepObra' : 'CEP',
            'infoGeral': 'Informações gerais'
        }

        widgets = {
            'nomeCliente': forms.TextInput(attrs={'class':'form-control'}),
            'pontoFocalCliente': forms.TextInput(attrs={'class':'form-control'}),
            'dataIncio': forms.TextInput(attrs={'class':'form-control'}),
            'dataFim': forms.TextInput(attrs={'class':'form-control'}),
            'gerenteContrato': forms.TextInput(attrs={'class':'form-control'}),
            'enderecoObra': forms.TextInput(attrs={'class':'form-control'}),
            'cidadeObra': forms.TextInput(attrs={'class':'form-control'}),
            'estadoObra': forms.TextInput(attrs={'class':'form-control'}),
            'cepObra': forms.TextInput(attrs={'class':'form-control'}),
            'infoGeral': forms.TextInput(attrs={'class':'form-control'}),

        }
