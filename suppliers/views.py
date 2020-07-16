from django.shortcuts import render
from suppliers.models import Suppliers
from .forms import SuppliersForm

def supplier_create(request):
    forms = SuppliersForm(request.POST or None)
    if forms.is_valid():
        forms.save()
    forms = SuppliersForm()
    context = {
        'forms': forms
    }
    return render(request, 'input-suppliers.html', context=context)

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
