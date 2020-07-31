# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib.auth.models import User
from django.db import models



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nomeCliente = models.CharField(max_length=40)
    pontoFocalCliente = models.CharField(max_length=40)
    dataIncio = models.DateField(verbose_name='Data de Início')
    dataFim = models.DateField(verbose_name='Data prevista para conclusão')
    gerenteContrato = models.CharField(max_length=40)
    enderecoObra = models.CharField(max_length=100)
    cidadeObra = models.CharField(max_length=100)
    estadoObra = models.CharField(max_length=100)
    cepObra = models.CharField(max_length=9)
    infoGeral = models.TextField(max_length=500)

    class Meta:
        db_table = 'Profile'

    def __str__(self):
        return self.nomeCliente
# Create your models here.


    def get_date_initial(self):
        return self.dataIncio.strftime('%Y-%m-%d')


    def get_date_final(self):
        return self.dataFim.strftime('%Y-%m-%d')
