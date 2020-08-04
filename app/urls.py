# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from app import views
from suppliers.views import supplier_details, supplier_create
from order.views import order_create, order_submit_view
from authentication.views import update_user, edit_user_view

urlpatterns = [

    # The home page
    path('', views.index, name='home'),
    path('suppliers.html', supplier_details), #TODO: SEMPRE CADASTRAR AQUI NO URLS DO APP
    path('input-suppliers.html', supplier_create),
    path('order.html', order_create),
    path('submit-order', order_submit_view),
    path('edit-user.html', update_user),
    path('submit-user', edit_user_view),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
