from tempfile import NamedTemporaryFile
from urllib.request import urlopen
from django.contrib import messages
from django.core.paginator import Paginator
import requests
from bs4 import BeautifulSoup
from django.core.files import File
from django.shortcuts import render, get_object_or_404, redirect

from .forms import ContactForm
from .models import News, Category
from django.utils import timezone



def home(request):
    news_items = News.objects.all().order_by('-date_published')  # Получаем все новости, сортируем по дате

    # Пагинация: отображаем по 12 новостей на страницу
    paginator = Paginator(news_items, 12)  # Пагинация по 12 новостей на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()  # Загружаем категории

    context = {
        'page_obj': page_obj,  # Передаем объект пагинации в контекст
        'categories': categories  # Также передаем категории
    }
    return render(request, 'news/index.html', context)

def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    news_items = News.objects.filter(category=category).order_by('-date_published')  # Новости по категории

    # Пагинация: по 12 новостей на страницу
    paginator = Paginator(news_items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Добавляем список всех категорий для отображения в боковом меню или в шапке
    categories = Category.objects.all()

    context = {
        'category': category,
        'page_obj': page_obj,  # Пагинация
        'categories': categories,  # Список всех категорий
    }
    return render(request, 'news/category.html', context)



def news_detail(request, news_id):
    news_item = get_object_or_404(News, id=news_id)
    categories = Category.objects.all()  # Чтобы меню категорий было доступно
    news_item.views +=1
    news_item.save()

    context = {
        'news_item': news_item,
        'categories': categories,
    }
    return render(request, 'news/news_detail.html', context)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение было успешно отправлено!')
            return redirect('contact')
    else:
        form = ContactForm()

    return render(request, 'news/contact.html', {'form': form})


