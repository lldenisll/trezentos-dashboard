from django.db import models

class Order(models.Model):
    # dados da empresa não preciso criar outro DB, só resgatar essas informações de acordo com o nome do fornecedor
    nome = models.CharField(max_length=100)
    # razaosocial = models.CharField(max_length=200)
    # cnpj = models.CharField(max_length=22)
    # ie = models.CharField(max_length=20)
    # banco = models.CharField(max_length=100)
    # conta = models.CharField(max_length=8)
    # agencia = models.CharField(max_length=6)

    # dados da entrega
    dataentrega = models.DateTimeField(verbose_name='Data da entrega')
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


# Create your models here.
