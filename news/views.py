from bs4 import BeautifulSoup
from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import News, Category, TelegramNews
from .forms import ContactForm

# Главная страница с фильтрацией по языку
def home(request, language='hy'):
    # Фильтруем новости по выбранному языку
    news_items = News.objects.filter(language=language).order_by('-date_published')  # Отбираем последние 12 новостей
    telegram_news = TelegramNews.objects.all().order_by('-date_published')[:15]  # Добавляем Telegram новости

    paginator = Paginator(news_items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()
    weather_info = get_weather()
    rates = get_currency_rates()

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'selected_language': language,  # Передаем выбранный язык в контекст
        'weather_info': weather_info,
        'rates': rates,  # Передаем курсы валют в контекст'
        'telegram_news': telegram_news,  # Добавляем Telegram новости в контексте'''
    }
    return render(request, 'news/index.html', context)



# Новости по категориям с фильтрацией по языку
def category_view(request, category_id, language='hy'):
    category = get_object_or_404(Category, id=category_id)
    # Фильтруем новости по категории и выбранному языку
    news_items = News.objects.filter(category=category, language=language).order_by('-date_published')

    paginator = Paginator(news_items, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = Category.objects.all()

    context = {
        'category': category,
        'page_obj': page_obj,
        'categories': categories,
        'selected_language': language,  # Передаем выбранный язык в контекст
    }
    return render(request, 'news/category.html', context)


# Детальная страница новости
def news_detail(request, news_id, language='hy'):
    # Учитываем выбранный язык при поиске новости
    news_item = get_object_or_404(News, id=news_id, language=language)
    categories = Category.objects.all()  # Чтобы меню категорий было доступно
    news_item.views += 1  # Увеличиваем просмотры
    news_item.save()

    world_news = News.objects.filter(category__name='ԱՇԽԱՐՀ', language=language).order_by('-date_published')[:6]
    armenia_news = News.objects.filter(category__name='ՀԱՅԱՍՏԱՆ', language=language).order_by('-date_published')[:6]
    sports_news = News.objects.filter(category__name='ՍՊՈՐՏ', language=language).order_by('-date_published')[:6]
    more_news = News.objects.filter(category__name='ԱՎԵԼԻՆ', language=language).order_by('-date_published')[:6]

    context = {
        'news_item': news_item,
        'categories': categories,
        'selected_language': language,  # Передаем язык в контекст
        'world_news': world_news,
        'armenia_news': armenia_news,
        'sports_news': sports_news,
        'more_news': more_news,
    }
    return render(request, 'news/news_detail.html', context)


# Страница контактов
def contact(request, language='hy'):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ваше сообщение было успешно отправлено!')
            return redirect('contact', language=language)
    else:
        form = ContactForm()

    context = {
        'form': form,
        'selected_language': language,  # Передача языка в контекст
    }
    return render(request, 'news/contact.html', context)




import requests

def get_weather():
    # Вставьте ваш API ключ
    api_key = '45871b150cb1a0c87ca2faae487d0cb8'
    city = 'Yerevan'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric&lang=ru'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        # Получаем температуру, описание погоды и код иконки
        temperature = int(data['main']['temp'])
        description = data['weather'][0]['description']
        icon_code = data['weather'][0]['icon']

        # Формируем URL для иконки
        icon_url = f'http://openweathermap.org/img/wn/{icon_code}@2x.png'

        # Формируем строку с результатом
        return {
            'city': city,
            'temperature': temperature,
            'description': description,
            'icon_url': icon_url
        }
    else:
        return None
# Использование функции
weather_info = get_weather()


def get_currency_rates():
    # URL для получения курсов валют
    url = 'https://www.rate.am/hy/armenian-dram-exchange-rates/banks'

    # Заголовок для маскировки под браузер
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
    }

    # Инициализация значений по умолчанию
    usd_amd, eur_amd, rub_amd = None, None, None

    try:
        # Получение данных с сайта
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Проверяем наличие ошибок

        # Парсим HTML-код
        soup = BeautifulSoup(response.text, 'lxml')

        # Находим все блоки с информацией о валюте
        data = soup.find_all('div', class_='group flex items-center h-10 bg-N30')

        # Проверяем, что получили хотя бы один блок с информацией
        if len(data) > 0:
            # Извлекаем данные по валютам USD, EUR и RUB
            for block in data:
                currency_blocks = block.find_all('div',
                                                 class_='flex items-center justify-center min-w-[9rem] w-[33.333%]')

                # USD Block
                usd_sell = currency_blocks[0].find_all('div', class_='w-1/2')[1].text.strip()
                usd_amd = usd_sell

                # EUR Block
                eur_sell = currency_blocks[1].find_all('div', class_='w-1/2')[1].text.strip()
                eur_amd = eur_sell

                # RUB Block
                rub_sell = currency_blocks[2].find_all('div', class_='w-1/2')[1].text.strip()
                rub_amd = rub_sell

                # Так как блок данных повторяется, выходим после первого блока
                break

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении курса валют: {e}")

    # Возвращаем курсы валют в виде словаря
    return {
        'usd_amd': usd_amd,
        'eur_amd': eur_amd,
        'rub_amd': rub_amd,
    }


rates = get_currency_rates()