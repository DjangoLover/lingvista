# -*- coding: utf-8 -*-
import json
from django.http import HttpResponse
from django.conf import settings
from django.views.decorators.http import require_GET
from mstranslator import Translator


@require_GET
def translate(request):
    lang_from = request.GET.get('lang_from', None)
    lang_to = request.GET['lang_to']
    text = request.GET['text']

    t = Translator(settings.MS_TRANSLATOR_CLIENT_ID, settings.MS_TRANSLATOR_CLIENT_SECRET)
    translation = t.translate(text, lang_from, lang_to)
    data = {'lang_from': 'ru', 'lang_to': 'en', 'text': translation}
    return HttpResponse(json.dumps(data), content_type="application/json")


@require_GET
def langs(request):
    t = Translator(settings.MS_TRANSLATOR_CLIENT_ID, settings.MS_TRANSLATOR_CLIENT_SECRET)
    data = t.get_langs()
    return HttpResponse(json.dumps(data), content_type="application/json")