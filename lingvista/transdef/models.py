# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models


class Language(models.Model):
    """
    Language avaliable for translation and definition
    """
    isocode = models.TextField("ISO language code", max_length=10)
    bingcode = models.TextField("Bing language code", max_length=10)
    wikicode = models.TextField("Wikipedia language code", max_length=10)
    name = models.TextField("Readable name")
    
    def __unicode__(self):
        return self.name


class TransDefLog(models.Model):
    """
    Model stores user search for translation or definition
    """
    account = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Account', related_name='log')
    source = models.TextField('Source text', max_length=200)
    translation = models.TextField('Translation', max_length=500)
    definition = models.TextField('Definiton', max_length=500)
    lang_from = models.ForeignKey('Language', name='Source language', related_name='source_set')
    lang_to = models.ForeignKey('Language', name='Target language', related_name='transdef_set')
    created_at = models.DateTimeField('Creation time', auto_now_add=True)

    def __unicode__(self):
        return u'{0}: {1}'.format(self.pk, self.source[:20])


