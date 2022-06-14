from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView


class MainView(TemplateView):
    template_name = 'mainapp/index.html'

class ContacntsView(TemplateView):
    template_name = 'mainapp/contacts.html'

class CoursesView(TemplateView):
    template_name = 'mainapp/courses_list.html'

class DocsView(TemplateView):
    template_name = 'mainapp/doc_site.html'

class LoginView(TemplateView):
    template_name = 'mainapp/login.html'

class NewsView(TemplateView):
    template_name = 'mainapp/news.html'
