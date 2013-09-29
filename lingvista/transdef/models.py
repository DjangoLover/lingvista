# -*- coding: utf-8 -*-
from django.db import models


class TransDefLog(models.Model):
    """
    Model stores user search for translation or definition
    """
    source = models.TextField('Source text', max_length='200')
    text = models.TextField('Translation or definiton', max_length='500')
    is_definition = models.BooleanField()
    is_translation = models.BooleanField()
    lang_from = models.ForeignKey('Language', name='Source language', related_name='source_set')
    lang_to = models.ForeignKey('Language', name='Target language', related_name='transdef_set')

    def __unicode__(self):
        return '{0}: {1}'.format(self.text[:50], self.score)


class Language(models.Model):
    """
    Language avaliable for translation and definition
    """
    isocode = models.TextField("ISO language code", max_length=10)
    bingcode = models.TextField("Bing language code", max_length=10)
    wikicode = models.TextField("Wikipedia language code", max_length=10)
    name = models.TextField("Readable name")