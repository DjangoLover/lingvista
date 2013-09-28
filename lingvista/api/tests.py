# -*- coding: utf-8 -*-
from django.test import TestCase

class SimpleTest(TestCase):
    def test_translate(self):
        response = self.client.get('/api/v1/translate/', {'text': u'Привет', 'lang_to': 'en'})
        self.assertEqual(response.status_code, 200)
