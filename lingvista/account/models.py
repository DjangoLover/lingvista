# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager

from lingvista.transdef.models import Language


class Account(AbstractUser):
    language = models.ForeignKey(Language, blank=True, null=True,
        verbose_name=u'Default translate language')

    objects = UserManager()


class DeliverySettings(models.Model):
    FREQUENCY_CHOICES = (
        ('day', 'Daily'),
        ('week', 'Weekly'),
        ('month', 'Monthly')
    )
    account = models.OneToOneField(Account, verbose_name=u'User',
                                   related_name='delivery_settings')
    enabled = models.BooleanField(u'Enable sending', default=True)
    email = models.EmailField(u'Email to send statistics')
    frequency = models.CharField(u'Frequency', choices=FREQUENCY_CHOICES,
        default=FREQUENCY_CHOICES[0][0], max_length=10)
    
    def __unicode__(self):
        return 
