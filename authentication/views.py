# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from django.contrib import messages
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.forms.utils import ErrorList
from django.http import HttpResponse
from .forms import LoginForm, SignUpForm, ProfileForm
from .models import Profile

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:    
                msg = 'Invalid credentials'    
        else:
            msg = 'Error validating the form'    

    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

def register_user(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        p_form=ProfileForm(request.POST)
        if form.is_valid() and p_form.is_valid():
            user = form.save()
            p_form = p_form.save(commit=False)
            p_form.user = user
            p_form.save()
            messages.success(request, f'Registration complete! You may log in!')

            #return redirect("/login/")
    else:
        form = SignUpForm(request.POST)
        p_form = ProfileForm(request.POST)

    return render(request, "accounts/register.html", {"form": form, "p_form":p_form})


def update_user(request):
    profile_id = request.GET.get('id')
    context = {}
    if profile_id:
        context['Profile'] = Profile.objects.get(id=profile_id)
    return render(request, 'edit-user.html')


def edit_user_view(request):
    if request.POST:
        pontoFocalCliente = request.POST.get('pontoFocalCliente')
        dataIncio = request.POST.get('dataIncio')
        dataFim = request.POST.get('dataFim')
        gerenteContrato = request.POST.get('gerenteContrato')
        enderecoObra = request.POST.get('enderecoObra')
        cidadeObra = request.POST.get('cidadeObra')
        estadoObra = request.POST.get('estadoObra')
        cepObra = request.POST.get('cepObra')
        infoGeral = request.POST.get('infoGeral')
        profile_id = request.POST.get('profile_id')
        Profile.objects.filter(id=profile_id).update(
            pontoFocalCliente=pontoFocalCliente,
            dataIncio=dataIncio,
            dataFim=dataFim,
            gerenteContrato=gerenteContrato,
            enderecoObra=enderecoObra,
            cidadeObra=cidadeObra,
            estadoObra=estadoObra,
            cepObra=cepObra,
            infoGeral=infoGeral
        )
    return render(request, 'page-user.html')