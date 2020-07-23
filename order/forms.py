from django import forms
from suppliers.models import Suppliers
#from .models import Order #TODO: remover comentário depois de migrar as tabelas em models

class OrderForm(forms.Form):

    nome = forms.ModelChoiceField(queryset=Suppliers.objects.all())
    # dataentrega
    # enderecoentrega
    # responsavel
    # telefoneresponsavel
    # nomedaobra #TODO: recebe o nome do usuário
    # numerooc
    # revisao
    # referencia
    # data
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
    disciplina = forms.ChoiceField(label="Disciplina", widget=forms.Select, choices=disciplinaop)
    options = [
        ('1', 'cliente'),
        ('2', 'T-60'),
    ]
    faturador = forms.ChoiceField(label="Faturamento para", widget=forms.Select, choices=options)

