# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.core.exceptions import ObjectDoesNotExist

from lingvista.account.forms import AccountForm, DeliverySettingsForm

def account_detail(request):
    form = AccountForm(request.POST or None, instance=request.user)
    if form.is_valid():
        form.save()
    return render(request, 'account/account_detail.html', {'form': form})

def account_statistics(request):
    
    try:
        instance = request.user.delivery_settings
    except ObjectDoesNotExist:
        instance = None
    
    form = DeliverySettingsForm(request.POST or None, instance=instance)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.account = request.user
        obj.save()
    return render(request, 'account/account_statistics.html', {'form': form})