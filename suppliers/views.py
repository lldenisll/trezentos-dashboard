from django.shortcuts import render
from suppliers.models import Suppliers



def supplier_details(request):
    fornecedores = Suppliers.objects.all()
    # context = {
    #     'nome': fornecedores.nome,
    #     'razaosocial':fornecedores.razaosocial,
    #     'cnpj': fornecedores.cnpj,
    #     'endereco':fornecedores.enderecom,
    #     'telefone':fornecedores.telefone
    # }

    context = {
        'fornecedor': fornecedores
    }
    return render(request, 'suppliers.html',context = context)
# Create your views here.
