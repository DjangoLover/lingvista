# -*- coding: utf-8 -*-
import wikipedia
import textwrap

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
        page = wikipedia.page(source, auto_suggest=True, redirect=True)
        if len(page.summary) > 200:
            summary = textwrap.wrap(page.summary, 197)[0] + '...'
        else:
            summary = page.summary, 197
        return page.url, summary
    except:
        return None, None
