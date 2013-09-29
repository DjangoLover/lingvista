# -*- coding: utf-8 -*-
from django import forms

from lingvista.account.models import Account, DeliverySettings


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ('language', )


class DeliverySettingsForm(forms.ModelForm):
    class Meta:
        model = DeliverySettings
        exclude = ('account', )