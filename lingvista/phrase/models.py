# -*- coding: utf-8 -*-
from mstranslator import Translator

from django.db import models
from django.conf import settings


class Phrase(models.Model):
    user = models.ForeignKey('auth.User')
    text = models.TextField(u'Text')
    score = models.PositiveIntegerField(u'Score', default=1)
    lang_from = models.CharField(u'Source language', max_length=255)
    lang_to = models.CharField(u'Target language', max_length=255)

    def get_translation(self):
        t = Translator(settings.MS_TRANSLATOR_CLIENT_ID, settings.MS_TRANSLATOR_CLIENT_SECRET)
        return t.translate(self.text, self.lang_from, self.lang_to)

    def get_definition(self):
        pass

    def touch(self):
        self.score += 1
        self.save()

    def __unicode__(self):
        return '{0}: {1}'.format(self.text[:50], self.score)
