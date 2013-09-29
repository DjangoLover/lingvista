# -*- coding: utf-8 -*-
from rest_framework import serializers

from lingvista.account.models import Account


class AccountSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ('language',)

    language = serializers.SerializerMethodField('get_language')

    def get_language(self, obj):
        return obj.language.isocode