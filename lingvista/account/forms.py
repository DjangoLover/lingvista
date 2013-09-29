# -*- coding: utf-8 -*-
from django import forms
from crispy_forms.helper import FormHelper

from lingvista.account.models import Account, DeliverySettings


class AccountForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AccountForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'

    class Meta:
        model = Account
        fields = ('language', )


class DeliverySettingsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DeliverySettingsForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'


    class Meta:
        model = DeliverySettings
        exclude = ('account', )