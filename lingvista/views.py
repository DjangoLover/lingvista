# -*- coding: utf-8 -*-
from django.shortcuts import render

from lingvista.phrase.models import Phrase


def index(request):
    return render(request, 'lingvista/index.html', {
        'phrase_list': Phrase.objects.order_by('-score')[:10]
    })
