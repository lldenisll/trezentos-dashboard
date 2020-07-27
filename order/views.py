from django.shortcuts import render
from suppliers.models import Suppliers
from .forms import OrderForm, OrderForm2

def order_create(request):
    forms = OrderForm(request.POST or None)
    forms2 = OrderForm2(request.POST or None)
    if forms.is_valid() and forms2.is_valid():
        forms.save()
        forms2.save()
    forms = OrderForm()
    forms2=OrderForm2()
    context = {
        'forms': forms,
        'forms2': forms2
    }
    return render(request, 'order.html', context=context)
# Create your views here.
