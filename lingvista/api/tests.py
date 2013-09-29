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
        self.assertEqual(response.data['lang_from'], 'ru')
        self.assertEqual(response.data['lang_to'], 'en')
        self.assertEqual(response.data['translation'], 'Hello')

    def test_define(self):
        response = self.client.get('/api/v1/transdef/', {'source': 'Wikipedia', 'lang_to': 'en'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['lang_from'], 'en')
        self.assertEqual(response.data['lang_to'], 'en')
        self.assertIn('Wikimedia Foundation', response.data['definition'])

    def test_translate_and_define(self):
        response = self.client.get('/api/v1/transdef/', {'source': 'Википедия', 'lang_to': 'en'})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['lang_from'], 'ru')
        self.assertEqual(response.data['lang_to'], 'en')
        self.assertIn('Wikimedia Foundation', response.data['definition'])

    def test_langs(self):
        response = self.client.get('/api/v1/langs/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(('en', 'English'), response.data)
