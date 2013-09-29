# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from lingvista.transdef.models import Language


class Account(AbstractUser):
    language = models.ForeignKey(Language, blank=True, null=True)

    objects = UserManager()

    def __unicode__(self):
        return self.email


class DeliverySettings(models.Model):
    FREQUENCY_CHOICES = (
        ('day', 'day'),
        ('week', 'week'),
        ('month', 'month')
    )
    account = models.OneToOneField(Account, verbose_name=u'User',
                                   related_name='delivery')
    enabled = models.BooleanField(u'Enable sending', default=True)
    email = models.EmailField(u'Email')
    frequency = models.CharField(u'Frequency', choices=FREQUENCY_CHOICES,
        max_length=10)
    
    def __unicode__(self):
        return 
    