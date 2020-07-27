from django import forms
from suppliers.models import Suppliers
from .models import Order
from authentication.forms import ProfileForm, Profile
from authentication.models import Profile, User


class OrderForm(forms.ModelForm):
    endereco=Profile.objects.filter(user='user').enderecoObra
    enderecoentrega = forms.CharField(label = 'Endereço de entrega',initial=endereco,widget=forms.TextInput(attrs={"class": "form-control"}))
    class Meta:
        model = Order

        fields = {
            'dataentrega': 'dataentrega',
            'responsavel': 'responsavel',
            'telefoneresponsavel': 'telefoneresponsavel',
            'nomedaobra': 'nomedaobra',  # TODO: recebe o nome do usuário
            'numerooc': 'numerooc',
            'revisao': 'revisao',
            'referencia': 'referencia',
            'data': 'data'
        }

        labels = {
            'dataentrega': 'Data da entrega',
            'enderecoentrega': 'Endereço da entrega',
            'responsavel': 'Responsável pelo recebimento',
            'telefoneresponsavel': 'Telefone do responsável',
            'nomedaobra': 'Nome da Obra',
            'numerooc': 'Número da OC',
            'revisao': 'Revisão',
            'referencia': 'Referência',
            'data': 'Data do pedido'
        }


        widgets = {
            'dataentrega': forms.TextInput(attrs={'class': 'form-control'}),
            'enderecoentrega': forms.TextInput(attrs={'class': 'form-control'}),
            'responsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'telefoneresponsavel': forms.TextInput(attrs={'class': 'form-control'}),
            'nomedaobra': forms.TextInput(attrs={'class': 'form-control'}),
            'numerooc': forms.TextInput(attrs={'class': 'form-control'}),
            'revisao': forms.TextInput(attrs={'class': 'form-control'}),
            'referencia': forms.TextInput(attrs={'class': 'form-control'}),
            'data': forms.TextInput(attrs={'class': 'form-control'}),
        }


class OrderForm2(forms.Form):
    nome = forms.ModelChoiceField(queryset=Suppliers.objects.all(),
                                  widget=forms.Select(attrs={"class": "form-control"}))
    disciplinaop = [
        ('1', 'Seguro'),
        ('2', 'Equipe de Obra'),
        ('3', 'Materiais Preliminares'),
        ('4', 'Mobilização'),
        ('5', 'Elevador/Plataforma'),
        ('6', 'Demolição'),
        ('7', 'Caçamba'),
        ('8', 'Civil'),
        ('9', 'Hidráulica'),
        ('10', 'Itens de incêndio'),
        ('11', 'Detecção'),
        ('12', 'Elétrica'),
        ('13', 'Ar condicionado'),
        ('14', 'Carpete'),
        ('15', 'Vinílico'),
        ('16', 'Rodapé'),
        ('17', 'Instalação de carpete e vinículo'),
        ('18', 'Porcelanato'),
        ('19', 'Gesso'),
        ('20', 'Pintura'),
        ('21', 'Div Vidro'),
        ('22', 'Portas'),
        ('23', 'Cadeiras'),
        ('24', 'Mobiliário de Trabalho'),
        ('25', 'Mobiliário decorativo'),
        ('26', 'Marcenaria'),
        ('27', 'Serralheria'),
        ('28', 'Marmoaria'),
        ('29', 'Locker'),
        ('30', 'Persianas'),
        ('31', 'Louças e metais'),
        ('32', 'Luminárias'),
        ('33', 'Comunicação visual'),
        ('34', 'Equipamentos'),
        ('35', 'Limpeza'),
        ('36', 'Paisagismo'),
    ]
    disciplina = forms.ChoiceField(label="Disciplina", widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=disciplinaop, initial='20')
    options = [
        ('1', 'cliente'),
        ('2', 'T-60'),
    ]
    faturador = forms.ChoiceField(label="Faturamento para", widget=forms.Select(attrs={"class": "form-control"}),
                                  choices=options)




