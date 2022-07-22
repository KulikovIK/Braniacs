from http import HTTPStatus
from django.test import TestCase
from django.urls import reverse

class StaticPagesSmokeTest(TestCase):
    def test_static_authapp_pages_open(self):
        urls_list = [
            'authapp:login',
            'authapp:register',
        ]

        for url in urls_list:
            url = reverse(url)
            result = self.client.get(url)

            self.assertEqual(result.status_code, HTTPStatus.OK)
