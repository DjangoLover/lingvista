# -*- coding: utf-8 -*-
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from lingvista.api.serializers import AccountSettingsSerializer
from lingvista.account.models import Account
from lingvista.transdef.utils import define, translate, detect_language
from lingvista.transdef.models import Language, TransDefLog



@api_view(['GET'])
def transdef(request):
    """
    Finds translation and definition of source text
    """
    lang_from = request.QUERY_PARAMS.get('lang_from', None)
    lang_to = request.QUERY_PARAMS['lang_to']
    lang_from = get_object_or_404(Language, isocode=lang_from) if lang_from else None
    lang_to = get_object_or_404(Language, isocode=lang_to)
    source = request.QUERY_PARAMS['source']

    if not lang_from:
        lang_from = detect_language(source)
    if lang_from != lang_to:
        translation = translate(source, lang_from, lang_to)
        # FIXME: definition -> null=True
        definition = define(translation, lang_to) or ''
        if request.user.is_authenticated():
            TransDefLog.objects.create(
                account=request.user,
                source=source,
                translation=translation,
                definition=definition,
                lang_from=lang_from,
                lang_to=lang_to
            )
    else:
        translation = None
        definition = define(source, lang_to)
    data = {
        'lang_from': lang_from.isocode,
        'lang_to': lang_to.isocode,
        'source': source,
        'translation': translation,
        'definition': definition,
    }
    return Response(data)


@api_view(['GET'])
def langs(request):
    """
    Returns supported languages
    """
    languages = Language.objects.all().values_list('isocode', 'name')
    return Response(languages)


class AccountSettingsView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Account.objects.all()
    serializer_class = AccountSettingsSerializer

    def get_object(self, queryset=None):
        return self.request.user

    def get_object_or_none(self):
        return self.request.user
