# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from lingvista.transdef.models import Language


class Account(AbstractUser):
    language = models.ForeignKey(Language, default=lambda: Language.objects.get(isocode='en'))

    objects = UserManager()

    def __unicode__(self):
        return self.email
