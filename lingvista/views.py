# -*- coding: utf-8 -*-
from django.contrib.auth import logout
from django.shortcuts import render, redirect


def index(request):
    return render(request, 'lingvista/index.html')


def logout_user(request):
    logout(request)
    return redirect('lingvista-index')