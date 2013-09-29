# -*- coding: utf-8 -*-
import datetime

from optparse import make_option

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand, CommandError

from django.template.loader import render_to_string

from lingvista.account.models import DeliverySettings
from lingvista.transdef.models import TransDefLog


def check_date(freq):
    if freq == 'day':
        return True
    today = datetime.date.today()
    if freq == 'week':
        return today.weekday() == 0
    if freq == 'month':
        return today.day == 1
    return False


class Command(BaseCommand):

    help = 'Send statistics to accounts'

    option_list = list(BaseCommand.option_list) + [
        make_option('-q', '--quiet', action='store_true', default=False, help="Quiet mode"),
    ]

    def handle(self, *args, **options):
        self.quiet = options.get('quiet', False)
        subject=u'Translate statistics from lingvista'
        today = datetime.date.today()
        for delivery_setting in DeliverySettings.objects.filter(enabled=True):
            if check_date(delivery_setting.freq):
                query = {}
                if freq == 'month':
                    query = {'creation_date__gte': today + datetime.timedelta(30)}
                if freq == 'week':
                    query = {'creation_date__gte': today + datetime.timedelta(7)}
                translate_list = delivery_setting.account.log.filter(**query)
                content = render_to_string('account/email/statistics_to_user.html',
                    {'delivery_setting': delivery_setting, 'log_list': 'log_list'})
                message = EmailMessage(subject, content, 'info@lingvista.com', [item.email])
                message.content_subtype = "html" 
                message.send()

