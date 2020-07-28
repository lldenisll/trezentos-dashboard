from django import forms
from suppliers.models import Suppliers
from .models import Order
from authentication.forms import ProfileForm, Profile
from authentication.models import Profile, User
import random
from datetime import date, timedelta

class OrderForm(forms.ModelForm):

    ocproduto = random.randint(1, 999)
    g_numerooc = f'{ocproduto} / {date.today().month}'
    g_dataentrega = date.today() + timedelta(days=5)
    g_endereco = Profile.objects.get(id=4).enderecoObra
    g_resp = Profile.objects.get(id=4).pontoFocalCliente
    g_nomeobra = Profile.objects.get(id=4).user
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
    options = [
        ('1', 'cliente'),
        ('2', 'T-60'),
    ]

    enderecoentrega = forms.CharField(label='Endereço de entrega', initial=g_endereco,
                                      widget=forms.TextInput(attrs={"class": "form-control"}))
    responsavel = forms.CharField(label='Responsável pela entrega', initial=g_resp,
                                  widget=forms.TextInput(attrs={"class": "form-control"}))
    nomedaobra = forms.CharField(label='Obra', initial=g_nomeobra,
                                 widget=forms.TextInput(attrs={"class": "form-control"}))
    numerooc = forms.CharField(label='Numero OC', initial=g_numerooc,
                               widget=forms.TextInput(attrs={"class": "form-control"}))
    dataentrega = forms.DateField(label='Data da entrega', initial=(g_dataentrega),
                                  widget=forms.DateInput(attrs={"class": "form-control"}))
    data = forms.DateField(label='Data da O.C', initial=date.today(),
                           widget=forms.DateInput(attrs={"class": "form-control"}))
    valor = forms.CharField(label='Valor da compra', initial='R$',
                            widget=forms.TextInput(attrs={"class": "form-control"}))
    DDL = forms.CharField(label='DDL', widget=forms.TextInput(attrs={"class": "form-control"}))
    datapg = forms.DateField(label='Data do pagamento', initial=date.today(),
                             widget=forms.DateInput(attrs={"class": "form-control"}))
    obs = forms.CharField(label='Observação', widget=forms.TextInput(attrs={"class": "form-control"}))
    descritivo = forms.CharField(label='Descritivo', widget=forms.TextInput(attrs={"class": "form-control"}))
    telefoneresponsavel = forms.CharField(label='Telefone do responsável',
                                          widget=forms.TextInput(attrs={"class": "form-control"}))
    revisao = forms.CharField(label='Revisão', widget=forms.TextInput(attrs={"class": "form-control"}))
    referencia = forms.CharField(label='Referencia', widget=forms.TextInput(attrs={"class": "form-control"}))
    nome = forms.ModelChoiceField(queryset=Suppliers.objects.all(),
                                  widget=forms.Select(attrs={"class": "form-control"}))
    disciplina = forms.ChoiceField(label="Disciplina", widget=forms.Select(attrs={"class": "form-control"}),
                                   choices=disciplinaop, initial='20')
    faturador = forms.ChoiceField(label="Faturamento para", widget=forms.Select(attrs={"class": "form-control"}),
                                  choices=options)

    class Meta:
        model = Order
        fields = ('nome',
        'dataentrega',
        'enderecoentrega',
        'responsavel',
        'telefoneresponsavel',
        'nomedaobra' ,
        'numerooc' ,
        'disciplina',
        'revisao' ,
        'referencia',
        'data' ,
        'valor' ,
        'DDL',
        'datapg',
        'obs' ,
        'descritivo',
        'faturador' )






#class OrderForm2(forms.Form):





