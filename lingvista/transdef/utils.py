# -*- coding: utf-8 -*-
from django.conf import settings
from mstranslator import Translator


def get_translation(source, lang_from, lang_to):
    t = Translator(settings.MS_TRANSLATOR_CLIENT_ID, settings.MS_TRANSLATOR_CLIENT_SECRET)
    return t.translate(source, lang_from, lang_to)


def get_definition(source, lang):
    pass
