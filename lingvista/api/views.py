# -*- coding: utf-8 -*-
from mstranslator import Translator
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from lingvista.transdef.utils import define, translate, detect_language
from lingvista.transdef.models import Language


@api_view(['GET'])
def transdef(request):
    """
    Finds translation and definition of source text
    """
    lang_from = request.QUERY_PARAMS.get('lang_from', None)
    lang_to = request.QUERY_PARAMS['lang_to']
    lang_from = get_object_or_404(Language, isocode=lang_from) if lang_from else None
    lang_to = get_object_or_404(Language, isocode=lang_to)
    source = request.QUERY_PARAMS['source']

    if not lang_from:
        lang_from = detect_language(source)
    translation = translate(source, lang_from, lang_to)
    #definition = define(source, lang_from, lang_to)
    data = {
        'lang_from': lang_from.isocode,
        'lang_to': lang_to.isocode,
        'text': translation
    }
    return Response(data)


@api_view(['GET'])
def langs(request):
    """
    Returns supported languages
    """
    languages = Language.objects.all().values_list('isocode', 'name')
    return Response(languages)
