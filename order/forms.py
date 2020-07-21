from django import forms
from suppliers.models import Suppliers

class OrderForm(forms.Form):

    supplier = forms.ModelChoiceField(queryset=Suppliers.objects.all())


