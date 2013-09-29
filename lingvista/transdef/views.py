# -*- coding: utf-8 -*-
from django.shortcuts import render


def trainer(request):
	return render(request, 'transdef/trainer.html', {})
