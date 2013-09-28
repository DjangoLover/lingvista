# -*- coding: utf-8 -*-
import json
from rest_framework.test import APITestCase


class APITest(APITestCase):
    """
    Test case for lingvista REST API
    """
    def test_translate(self):
        response = self.client.get('/api/v1/translate/', {'text': 'Привет', 'lang_to': 'en'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'lang_from': 'ru', 'lang_to': 'en', 'text': 'Hello'})

    def test_langs(self):
        response = self.client.get('/api/v1/langs/')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertIn('en', response.data)