# -*- coding: utf-8 -*-
from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models

from lingvista.transdef.models import Language


class Account(AbstractUser):
    language = models.ForeignKey(Language, blank=True, null=True, verbose_name='Default translate language')

    objects = UserManager()


class DeliverySettings(models.Model):
    FREQUENCY_CHOICES = (
        ('day', 'Daily'),
        ('week', 'Weekly'),
        ('month', 'Monthly')
    )
    account = models.OneToOneField(Account, verbose_name='User', related_name='delivery_settings')
    enabled = models.BooleanField('Enable sending', default=True)
    email = models.EmailField('Email to send statistics')
    frequency = models.CharField('Frequency', choices=FREQUENCY_CHOICES,
                                 default=FREQUENCY_CHOICES[0][0], max_length=10)
