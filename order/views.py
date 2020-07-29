from django.shortcuts import render
from suppliers.models import Suppliers
from .forms import OrderForm
from authentication.models import Profile,User

def order_create(request,profile_id):
    profile_id =  Profile.objects.all().last().id #TODO: trocar a forma como pega o ID para request.id
    forms = OrderForm(request.POST or None)
    if forms.is_valid():
        forms.save()
    forms = OrderForm()
    context = {
        'forms': forms
    }
    return render(request, 'order.html', context=context)



# Create your views here.
