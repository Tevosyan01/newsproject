from django.urls import path
from. import views

urlpatterns = [
    path('', views.home,name='home'),
    path('category/<int:category_id>/', views.category_view, name='category_view'),
    path('news/<int:news_id>/', views.news_detail, name='news_detail'),  # Новый путь
    path('contact/', views.contact, name='contact'),
]