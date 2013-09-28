# -*- coding: utf-8 -*-
import json
from django.test import TestCase

class APITest(TestCase):
    def test_translate(self):
        response = self.client.get('/api/v1/translate/', {'text': u'Привет', 'lang_to': 'en'})
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['text'], 'Hello')

    def test_langs(self):
        response = self.client.get('/api/v1/langs/')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(data, list)
        self.assertIn('en', data)