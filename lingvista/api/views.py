# -*- coding: utf-8 -*-
from django.conf import settings
from mstranslator import Translator
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET'])
def translate(request):
    lang_from = request.QUERY_PARAMS.get('lang_from', None)
    lang_to = request.QUERY_PARAMS['lang_to']
    text = request.QUERY_PARAMS['text']

    t = Translator(settings.MS_TRANSLATOR_CLIENT_ID, settings.MS_TRANSLATOR_CLIENT_SECRET)
    translation = t.translate(text, lang_from, lang_to)
    data = {'lang_from': 'ru', 'lang_to': 'en', 'text': translation}
    return Response(data)


@api_view(['GET'])
def langs(request):
    t = Translator(settings.MS_TRANSLATOR_CLIENT_ID, settings.MS_TRANSLATOR_CLIENT_SECRET)
    data = t.get_langs()
    return Response(data)