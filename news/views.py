from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib import messages
from .models import News, Category
from .forms import ContactForm

# Главная страница с фильтрацией по языку
def home(request, language='hy'):
    # Фильтруем новости по выбранному языку
    news_items = News.objects.filter(language=language).order_by('-date_published')

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
        temperature = data['main']['temp']
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
    # Ваш API ключ
    api_key = '24d19ce1c4fa0e854fef8aed'

    # URL для получения курсов валют для USD, EUR и RUB
    url_usd = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    url_eur = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/EUR'
    url_rub = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/RUB'

    # Инициализация значений по умолчанию
    usd_amd, eur_amd, rub_amd = None, None, None

    # Получение курсов валют
    try:
        response_usd = requests.get(url_usd)
        if response_usd.status_code == 200:
            data_usd = response_usd.json()
            usd_amd = data_usd['conversion_rates']['AMD']

        response_eur = requests.get(url_eur)
        if response_eur.status_code == 200:
            data_eur = response_eur.json()
            eur_amd = data_eur['conversion_rates']['AMD']

        response_rub = requests.get(url_rub)
        if response_rub.status_code == 200:
            data_rub = response_rub.json()
            rub_amd = data_rub['conversion_rates']['AMD']

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при получении курса валют: {e}")

    # Возвращаем курсы валют в виде словаря
    return {
        'usd_amd': usd_amd,
        'eur_amd': eur_amd,
        'rub_amd': rub_amd,
    }

rates = get_currency_rates()