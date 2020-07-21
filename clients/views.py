from django.shortcuts import render
from .models import Client
from .forms import ClientForm

def client_create(request):
    forms = ClientForm(request.POST or None)
    if forms.is_valid():
        forms.save()
    forms = ClientForm()
    context = {
        'forms': forms
    }
    return render(request, 'ui-notifications.html', context=context)
# Create your views here.
