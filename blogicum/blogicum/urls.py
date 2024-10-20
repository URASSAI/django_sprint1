from django.contrib import admin
from django.urls import path, include

# Инициализация ссылок на страницы admin, blog и pages.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace='pages')),
    path('', include('blog.urls', namespace='blog'))
]
