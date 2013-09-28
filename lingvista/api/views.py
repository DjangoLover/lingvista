# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse


def translate(request):
    data = {'lang_from': 'ru', 'lang_to': 'en', 'text': 'Hello'}
    return HttpResponse(json.dumps(data), content_type="application/json")