from django.urls import path
from mainapp.views import MainView, ContacntsView, CoursesView, DocsView, LoginView, NewsView, SearchView, NewsDetailView, NewsDeleteView, NewsCreateView, NewsUpdateView, CourseDetailView, CourseFeedbackCreateView
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path('', MainView.as_view(), name='index'),
    path('contacts/', ContacntsView.as_view(), name='contacts'),

    # Courses
    path('courses/', CoursesView.as_view(), name='courses'),
    path('courses/<int:pk>/detail/', CourseDetailView.as_view(), name='courses_detail'),
    path('courses/feedback/', CourseFeedbackCreateView.as_view(), name='course_feedback'),

    path('doc_site/', DocsView.as_view(), name='docs'),
    path('login/', LoginView.as_view(), name='login'),

    # News
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/detail/', NewsDetailView.as_view(), name='news_detail'),
    path('news/<int:pk>/delete/', NewsDeleteView.as_view(), name='news_delete'),
    path('news/<int:pk>/update/', NewsUpdateView.as_view(), name='news_update'),
    path('news/create/', NewsCreateView.as_view(), name='news_create'),

    # other
    path('search/', SearchView.as_view(), name='search'),
]

