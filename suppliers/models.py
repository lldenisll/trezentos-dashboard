from django.db import models

class Suppliers(models.Model):

    nome = models.CharField(max_length=100)
    razaosocial = models.CharField(max_length=200)
    cnpj = models.CharField(max_length=22)
    ie = models.CharField(max_length=20)
    enderecom = models.CharField(max_length=300)
    telefone = models.CharField(max_length=12) #TODO: Change for phoneField https://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    email = models.EmailField(max_length = 254)
    contato = models.CharField(max_length=100)
    banco = models.CharField(max_length=100)
    conta = models.CharField(max_length=8)
    agencia = models.CharField(max_length=6)

# Create your models here.
