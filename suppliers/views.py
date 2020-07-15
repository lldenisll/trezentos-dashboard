from django.shortcuts import render
from suppliers.models import Suppliers



def supplier_details(request):
    fornecedores = Suppliers.objects.get(id=1)
    context = {
        'nome': fornecedores.nome,
        'razaosocial':fornecedores.razaosocial
    }
    return render(request, 'suppliers.html',context)
# Create your views here.
