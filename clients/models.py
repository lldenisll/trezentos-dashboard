from django.db import models


class Client(models.Model):
    nomeCliente = models.CharField(max_length=40)
    pontoFocalCliente = models.CharField(max_length=40)
    dataIncio = models.DateTimeField(verbose_name='Data de Início')
    dataFim = models.DateTimeField(verbose_name='Data prevista para conclusão')
    gerenteContrato = models.CharField(max_length=40)
    enderecoObra = models.CharField(max_length=100)
    cidadeObra = models.CharField(max_length=100)
    estadoObra = models.CharField(max_length=100)
    cepObra = models.CharField(max_length=9)
    infoGeral = models.CharField(max_length=500)

    class Meta:
        db_table='Client'
    def __str__(self):
        return self.nome


# Create your models here.
