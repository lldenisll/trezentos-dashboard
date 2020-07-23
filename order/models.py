from django.db import models

class Order(models.Model):
    nome = models.CharField(max_length=100)
    # dados da entrega
    dataentrega = models.DateField(verbose_name='Data da entrega')
    enderecoentrega = models.CharField(max_length=300)
    responsavel = models.CharField(max_length=100)
    telefoneresponsavel = models.CharField(max_length=12)

    # Dados da obra

    nomedaobra = models.CharField(max_length=100) #TODO: ver aonde colocar o nome da obra para pegar info automattica
    numerooc = models.CharField(max_length=4)
    disciplina = models.CharField(max_length=40) #TODO: ver caracteres e p/ todos abaixo se precisa
    revisao = models.CharField(max_length=40)
    referencia = models.CharField(max_length=40)
    data = models.DateTimeField(verbose_name='Data da OC')

    # Dados de pagamento
    valor = models.CharField(max_length=12)
    DDL = models.CharField(max_length=3)
    datapg = models.DateField(verbose_name='Data de pagamento')
    obs = models.CharField(max_length=50)
    descritivo = models.TextField(max_length=500)

    # Dados de faturamento
    faturador = models.TextField(max_length=23)
# Create your models here.
