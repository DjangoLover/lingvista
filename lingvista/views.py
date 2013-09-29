# -*- coding: utf-8 -*-
from django.db.models import Count
from django.contrib.auth import logout
from django.shortcuts import render, redirect

from lingvista.transdef.models import TransDefLog

def index(request):
    log_list = TransDefLog.objects.values('source').annotate(total=Count('source')).order_by('-total')

    return render(request, 'lingvista/index.html', {
        'log_list': log_list
    })


def logout_user(request):
    logout(request)
    return redirect('lingvista-index')