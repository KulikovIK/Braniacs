from datetime import datetime
from urllib import request, response
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'mainapp/index.html'

class ContacntsView(TemplateView):
    template_name = 'mainapp/contacts.html'


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_data'] = [
            {
                'city': 'Санкт‑Петербург',
                'phone': '+7-999-11-11111',
                'email': 'geeklab@spb.ru',
                'addr': 'территория Петропавловская крепость, 3Ж',
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHcrhA',
            }, {
                'city': 'Казань',
                'phone': '+7-999-22-22222',
                'email': 'geeklab@kz.ru',
                'addr': 'территория Кремль, 11, Казань, Республика Татарстан, Россия',
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHX3xB',
            }, {
                'city': 'Москва',
                'phone': '+7-999-33-33333',
                'email': 'geeklab@msk.ru',
                'addr': 'Красная площадь, 7, Москва, Россия',
                'map': 'https://yandex.ru/map-widget/v1/-/CCUAZHh9kD',
            },
        ]
        return context_data

class CoursesView(TemplateView):
    template_name = 'mainapp/courses_list.html'

class DocsView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class LoginView(TemplateView):
    template_name = 'mainapp/login.html'

class NewsView(TemplateView):
    template_name = 'mainapp/news.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = [
            {
                'title': 'Новость 1',
                'preview': 'Превью новости 1',
                'date': datetime.now()
            }, {
                'title': 'Новость 2',
                'preview': 'Превью новости 2',
                'date': '2022-01-01'
            }, {
                'title': 'Новость 3',
                'preview': 'Превью новости 3',
                'date': '2022-01-01'
            }, {
                'title': 'Новость 4',
                'preview': 'Превью новости 4',
                'date': '2022-01-01'
            }, {
                'title': 'Новость 1',
                'preview': 'Превью новости 4',
                'date': '2022-01-01'
            }, 
        ]
        return context_data

class SearchView(View):
    def get(self, request):
        response = request.GET['param'].replace(' ', '+')
        return redirect(f'https://yandex.ru/search/?text={response}&lr=11219')
    
    
