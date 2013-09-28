# -*- coding: utf-8 -*-
from mstranslator import Translator
from rest_framework.decorators import api_view
from rest_framework.response import Response

from lingvista.transdef.utils import get_definition, get_translation
from lingvista.transdef.models import Language


@api_view(['GET'])
def translate(request):
    """
    Translates
    """
    lang_from = request.QUERY_PARAMS.get('lang_from', None)
    lang_to = request.QUERY_PARAMS['lang_to']
    source = request.QUERY_PARAMS['source']
    translation = get_translation(source, lang_from, lang_to)
    data = {'lang_from': 'ru', 'lang_to': 'en', 'text': translation}
    return Response(data)


@api_view(['GET'])
def langs(request):
    """
    Returns supported languages.
    """
    languages = Language.objects.all().values_list('isocode', 'name')
    return Response(languages)
