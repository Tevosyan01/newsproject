from django.urls import path
from django.shortcuts import redirect  # Используем правильный импорт
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', lambda request: redirect('home', language='hy')),
    path('<str:language>/', views.home, name='home'),
    path('<str:language>/category/<int:category_id>/', views.category_view, name='category_view'),
    path('<str:language>/news/<int:news_id>/', views.news_detail, name='news_detail'),
    path('<str:language>/contact/', views.contact, name='contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)