from django.urls import path
from mainapp import views
from django.views.decorators.cache import cache_page
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', views.MainView.as_view(), name='index'),
    path('contacts/', views.ContacntsView.as_view(), name='contacts'),
    path('doc_site/', views.DocsView.as_view(), name='docs'),
    path('login/', views.LoginView.as_view(), name='login'),

    # Courses
    path('courses/', cache_page(360)(views.CoursesView.as_view()), name='courses'),
    path('courses/<int:pk>/detail/', views.CourseDetailView.as_view(), name='courses_detail'),
    path('courses/feedback/', views.CourseFeedbackCreateView.as_view(), name='course_feedback'),

    # News
    path('news/', views.NewsView.as_view(), name='news'),
    path('news/<int:pk>/detail/', views.NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/delete/', views.NewsDeleteView.as_view(), name='news_delete'),
    path('news/<int:pk>/update/', views.NewsUpdateView.as_view(), name='news_update'),
    path('news/create/', views.NewsCreateView.as_view(), name='news_create'),

    # Logs
    path('logs/', views.LogView.as_view(), name='logs_list'),
    path('logs/download/', views.LogDownloadView.as_view(), name='logs_download'),

    # other
    path('search/', views.SearchView.as_view(), name='search'),
  ]

