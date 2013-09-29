# -*- coding: utf-8 -*-
import wikipedia
from django.conf import settings
from mstranslator import Translator

from lingvista.transdef.models import Language


def detect_language(source):
    """
    Detects language of source text
    """
    t = Translator(settings.MS_TRANSLATOR_CLIENT_ID, settings.MS_TRANSLATOR_CLIENT_SECRET)
    bingcode = t.detect_lang(source)
    return Language.objects.get(bingcode=bingcode)


def translate(source, lang_from, lang_to):
    """
    Translates source text from and to scpecified language
    """
    lang_from_bingcode = lang_from.bingcode if lang_from else None
    t = Translator(settings.MS_TRANSLATOR_CLIENT_ID, settings.MS_TRANSLATOR_CLIENT_SECRET)
    return t.translate(source, lang_from_bingcode, lang_to.bingcode)


def define(source, lang):
    """
    Finds definition of source text in specified language
    """
    wikipedia.set_lang(lang.wikicode)
    try:
        return wikipedia.summary(source, chars=200)
    except:
        return None
