# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser


class Account(AbstractUser):
    lang = models.CharField(u'Language', max_length=255)

    def __unicode__(self):
        return self.email
