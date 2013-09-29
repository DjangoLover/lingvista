# -*- coding: utf-8 -*-
from django.db.models import Count
from django.shortcuts import render

from lingvista.transdef.models import TransDefLog


def trainer(request):
    log_list = TransDefLog.objects.values('source', 'lang_from__isocode', 'lang_to__isocode',
                                           'translation', 'definition') \
                                  .annotate(total=Count('source')) \
                                  .order_by('-total')
    return render(request, 'transdef/trainer.html', {
        'log_list': log_list
    })
