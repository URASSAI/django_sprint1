from django.urls import path

from . import views
# Namespace для приложения pages.
app_name = 'pages'
# Инициализация ссылок на страницы about и rules.
urlpatterns = [
    path('about/', views.about, name='about'),
    path('rules/', views.rules, name='rules')
]