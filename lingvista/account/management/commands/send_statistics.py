# -*- coding: utf-8 -*-
import datetime

from optparse import make_option

from django.conf import settings
from django.core.mail import EmailMessage
from django.core.management.base import BaseCommand, CommandError

from django.template.loader import render_to_string

from lingvista.account.models import DeliverySettings
from lingvista.transdef.models import TransDefLog


class Command(BaseCommand):

    help = 'Send statistics to accounts'

    option_list = list(BaseCommand.option_list) + [
        make_option('-q', '--quiet', action='store_true', default=False, help="Quiet mode"),
        make_option('-f', '--force', action='store_true', default=False, help="Force all checks"),
    ]

    def check_date(self, freq):
        if self.force_check:
            return True
        if freq == 'day':
            return True
        today = datetime.date.today()
        if freq == 'week':
            return today.weekday() == 0
        if freq == 'month':
            return today.day == 1
        return False

    def handle(self, *args, **options):
        self.quiet = options.get('quiet', False)
        self.force_check = options.get('force', False)
        subject=u'Translate statistics from lingvista'
        today = datetime.date.today()
        for delivery_setting in DeliverySettings.objects.filter(enabled=True):
            freq = delivery_setting.frequency
            if self.check_date(freq):
                query = {}
                if freq == 'day':
                    query = {'creation_date__gte': today + datetime.timedelta(1)}
                if freq == 'week':
                    query = {'creation_date__gte': today + datetime.timedelta(7)}
                if freq == 'month':
                    query = {'creation_date__gte': today + datetime.timedelta(30)}
                log_list = delivery_setting.account.log.filter(**query)
                content = render_to_string('account/email/statistics_to_user.html',
                    {'delivery_setting': delivery_setting, 'log_list': log_list})
                message = EmailMessage(subject, content, settings.MAIL_FROM, [delivery_setting.email])
                message.content_subtype = "html" 
                message.send()

