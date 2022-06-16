from django.urls import path
from mainapp.views import MainView, ContacntsView, CoursesView, DocsView, LoginView, NewsView, SearchView
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('contacts/', ContacntsView.as_view(), name='contacts'),
    path('courses_list/', CoursesView.as_view(), name='courses'),
    path('doc_site/', DocsView.as_view(), name='docs'),
    path('login/', LoginView.as_view(), name='login'),
    path('news/', NewsView.as_view(), name='news'),
    path('search/', SearchView.as_view(), name='search'),
]

