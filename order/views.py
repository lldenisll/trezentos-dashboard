from django.shortcuts import render
#from suppliers.models import Suppliers
#from authentication.models import Profile, User
from .models import Order

def order_create(request):
    order_id = request.GET.get('id')
    context = {}
    if order_id:
        context['Order'] = Order.objects.get(id=order_id)
    return render(request, 'order.html')

def order_submit_view(request):
    if request.POST:
        nome = request.POST.get('nome')
        dataentrega = request.POST.get('dataentrega')
        enderecoentrega = request.POST.get('enderecoentrega') # TODO: pegar valores do usuario atual
        responsavel = request.POST.get('responsavel') # TODO: pegar valores do usuario atual
        telefoneresponsavel = request.POST.get('telefoneresponsavel')
        nomedaobra = request.POST.get('nomedaobra') # TODO: pegar valores do usuario atual
        numerooc = request.POST.get('numerooc')
        disciplina = request.POST.get('disciplina')  # TODO: ver caracteres e p/ todos abaixo se precisa
        revisao = request.POST.get('revisao')
        referencia = request.POST.get('referencia')
        data = request.POST.get('data')
        valor = request.POST.get('valor')
        DDL = request.POST.get('DDL')
        datapg = request.POST.get('datapg')
        obs = request.POST.get('obs')
        descritivo = request.POST.get('descritivo')
        faturador = request.POST.get('faturador')
        order_id = request.POST.get('order_id')
        Order.objects.filter(id=order_id).create(
            nome=nome,
            dataentrega=dataentrega,
            enderecoentrega=enderecoentrega,
            responsavel=responsavel,
            telefoneresponsavel=telefoneresponsavel,
            nomedaobra=nomedaobra,
            numerooc=numerooc,
            disciplina=disciplina,
            revisao=revisao,
            referencia=referencia,
            data=data,
            valor=valor,
            DDL=DDL,
            datapg=datapg,
            obs=obs,
            descritivo=descritivo,
            faturador=faturador,
        )
    return render(request, 'order.html')


# Create your views here.
