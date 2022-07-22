from django.core import mail
from django.test import Client, TestCase
from django.urls import reverse
from http import HTTPStatus
from mainapp.models import News
from authapp.models import User
from mainapp.tasks import send_feedback_to_email

class StaticPagesSmokeTest(TestCase):
    def test_static_mainapp_pages_open(self):
        urls_list = [
            'mainapp:index',
            'mainapp:contacts',
            'mainapp:docs',
        ]

        for url in urls_list:
            url = reverse(url)
            result = self.client.get(url)

            self.assertEqual(result.status_code, HTTPStatus.OK)

class NewsTestCase(TestCase):

    def setUp(self) -> None:
        for i in range(10):
            News.objects.create(
                title=f'News_{i}',
                preview=f'Preview_{i}',
                body=f'Body_{i}',
            )
        User.objects.create_superuser(
            username='django',
            password='geekbrains'
        )
        self.client_with_auth = Client()
        auth_url = reverse('authapp:login')
        self.client_with_auth.post(
            auth_url,
            {
                'username': 'django', 
                'password': 'geekbrains'
            }
        )
    
    def test_open_page(self):
        url = reverse('mainapp:news')
        result = self.client.get(url)

        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_failed_open_create_by_anonym(self):
        url = reverse('mainapp:news_create')

        result = self.client.get(url)
        self.assertEqual(result.status_code, HTTPStatus.FOUND)

    def test_success_open_create_by_admin(self):
        
        news_counter = News.objects.all().count()
        
        url = reverse('mainapp:news_create')

        result = self.client_with_auth.post(
            url,
            data={
                'title':'News',
                'preview':'Preview',
                'body':'Body',
            }
        )
        self.assertEqual(
            result.status_code, 
            HTTPStatus.FOUND
        )

        self.assertEqual(
            News.objects.all().count(), 
            news_counter+1
        )

class MailSendTest(TestCase):

    def test_mail_send(self):
        message_text = 'test_message'
        send_feedback_to_email(message_body = message_text)

        self.assertEqual(
            mail.outbox[0].body,
            message_text
        )

    
