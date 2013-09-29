# -*- coding: utf-8 -*-
from rest_framework.test import APITestCase


class APITest(APITestCase):
    """
    Test case for lingvista REST API
    """
    fixtures = ['initial_data']

    def test_translate(self):
        response = self.client.get('/api/v1/transdef/', {'source': 'Привет', 'lang_to': 'en'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'lang_from': 'ru', 'lang_to': 'en', 'text': 'Hello'})

    def test_langs(self):
        response = self.client.get('/api/v1/langs/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(('en', 'English'), response.data)
