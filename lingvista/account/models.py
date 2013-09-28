# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Account(AbstractBaseUser):
    lang = models.CharField(u'Language', max_length=255)

    objects = AccountManager()

    def __unicode__(self):
        return self.email
