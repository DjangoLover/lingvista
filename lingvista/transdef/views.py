# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.shortcuts import render

from lingvista.transdef.models import TransDefLog

@login_required
def trainer(request):
    log_list = TransDefLog.objects.filter(account=request.user).select_related('lang_from', 'lang_to')
    return render(request, 'transdef/trainer.html', {
        'log_list': log_list
    })
