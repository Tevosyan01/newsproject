from django.core.management.base import BaseCommand
from news.models import News, Category
from bs4 import BeautifulSoup
import requests
from time import sleep
from django.utils import timezone


class Command(BaseCommand):
    help = 'Скрапинг новостей на русском языке для категорий "Мировые новости", "Спорт" и "Россия"'

    def handle(self, *args, **kwargs):
        self.scrape_aravot_russian_press()
        self.scrape_aravot_russian_sport()
        self.scrape_aravot_russian_culture()
        self.scrape_aravot_russian_rights()
        self.scrape_aravot_russian_politics()
        self.scrape_168am_russian_medic()
        self.scrape_168am_russian_sports()
        self.scrape_168am_russian_faces()
        self.scrape_168am_russian_busniess()

        # Другие категории можно добавить аналогично...


    def scrape_aravot_russian_press(self):
        print("Скрапинг новостей на английском для категории 'Politics'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.aravot.am/category/news/press/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для английских новостей
        category_english = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            title_tag = data.find('h1', class_='display-7')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='post_content')
            content = content_tag.text if content_tag else 'Контент не найден'

            # Парсим изображение
            image_tags = data.find_all('img', class_='rounded w-100 wp-post-image')
            image_url = None
            for img in image_tags:
                image_url = img.get('src') if img else 'Изображение не найдено'
                if image_url and not image_url.startswith('data:image/svg'):
                    break  # Прерываем цикл после нахождения первого подходящего изображения

            # Сохраняем новость в базу данных, если она еще не существует
            if not News.objects.filter(title=title, language='ru').exists():
                News.objects.create(
                    title=title,
                    content=content,
                    image=image_url,
                    category=category_english,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на английском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    def scrape_aravot_russian_sport(self):
        print("Скрапинг новостей на английском для категории 'Politics'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.aravot.am/category/news/sport/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для английских новостей
        category_english = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            title_tag = data.find('h1', class_='display-7')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='post_content')
            content = content_tag.text if content_tag else 'Контент не найден'

            # Парсим изображение
            image_tags = data.find_all('img', class_='rounded w-100 wp-post-image')
            image_url = None
            for img in image_tags:
                image_url = img.get('src') if img else 'Изображение не найдено'
                if image_url and not image_url.startswith('data:image/svg'):
                    break  # Прерываем цикл после нахождения первого подходящего изображения

            # Сохраняем новость в базу данных, если она еще не существует
            if not News.objects.filter(title=title, language='ru').exists():
                News.objects.create(
                    title=title,
                    content=content,
                    image=image_url,
                    category=category_english,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на английском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')

    def scrape_aravot_russian_culture(self):
        print("Скрапинг новостей на английском для категории 'Politics'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.aravot.am/category/news/culture/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для английских новостей
        category_english = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            title_tag = data.find('h1', class_='display-7')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='post_content')
            content = content_tag.text if content_tag else 'Контент не найден'

            # Парсим изображение
            image_tags = data.find_all('img', class_='rounded w-100 wp-post-image')
            image_url = None
            for img in image_tags:
                image_url = img.get('src') if img else 'Изображение не найдено'
                if image_url and not image_url.startswith('data:image/svg'):
                    break  # Прерываем цикл после нахождения первого подходящего изображения

            # Сохраняем новость в базу данных, если она еще не существует
            if not News.objects.filter(title=title, language='ru').exists():
                News.objects.create(
                    title=title,
                    content=content,
                    image=image_url,
                    category=category_english,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на английском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    def scrape_aravot_russian_rights(self):
        print("Скрапинг новостей на английском для категории 'Politics'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.aravot.am/category/news/rights/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для английских новостей
        category_english = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            title_tag = data.find('h1', class_='display-7')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='post_content')
            content = content_tag.text if content_tag else 'Контент не найден'

            # Парсим изображение
            image_tags = data.find_all('img', class_='rounded w-100 wp-post-image')
            image_url = None
            for img in image_tags:
                image_url = img.get('src') if img else 'Изображение не найдено'
                if image_url and not image_url.startswith('data:image/svg'):
                    break  # Прерываем цикл после нахождения первого подходящего изображения

            # Сохраняем новость в базу данных, если она еще не существует
            if not News.objects.filter(title=title, language='ru').exists():
                News.objects.create(
                    title=title,
                    content=content,
                    image=image_url,
                    category=category_english,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на английском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    def scrape_aravot_russian_politics(self):
        print("Скрапинг новостей на английском для категории 'Politics'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.aravot.am/category/news/politics/'
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для английских новостей
        category_english = Category.objects.get_or_create(name='ՀԱՅԱՍՏԱՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            title_tag = data.find('h1', class_='display-7')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='post_content')
            content = content_tag.text if content_tag else 'Контент не найден'

            # Парсим изображение
            image_tags = data.find_all('img', class_='rounded w-100 wp-post-image')
            image_url = None
            for img in image_tags:
                image_url = img.get('src') if img else 'Изображение не найдено'
                if image_url and not image_url.startswith('data:image/svg'):
                    break  # Прерываем цикл после нахождения первого подходящего изображения

            # Сохраняем новость в базу данных, если она еще не существует
            if not News.objects.filter(title=title, language='ru').exists():
                News.objects.create(
                    title=title,
                    content=content,
                    image=image_url,
                    category=category_english,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на английском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    def scrape_168am_russian_faces(self):
        print("Скрапинг новостей на русском для категории 'Мировые новости'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.168.am/category/face'  # Замените на реальный URL
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='realated-item clearfix')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_russian = Category.objects.get_or_create(name='ԱՇԽԱՐՀ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='single-content')

            title_tag = data.find('h1', class_='single-title')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='single-content-wrapper')
            content = content_tag.text if content_tag else 'Контент не найден'

            image_tag = data.find('img', class_='attachment-full size-full wp-post-image')
            image = image_tag.get('src') if image_tag else 'Изображение не найдено'

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title, language='ru').exists():
                # Сохранение новости в базу данных с указанием русского языка
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_russian,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на русском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')




    def scrape_168am_russian_sports(self):
        print("Скрапинг новостей на русском для категории 'ՍՊՈՐՏ'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.168.am/category/sport-ru'  # Замените на реальный URL
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='realated-item clearfix')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_russian = Category.objects.get_or_create(name='ՍՊՈՐՏ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='single-content')

            title_tag = data.find('h1', class_='single-title')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='single-content-wrapper')
            content = content_tag.text if content_tag else 'Контент не найден'

            image_tag = data.find('img', class_='attachment-full size-full wp-post-image')
            image = image_tag.get('src') if image_tag else 'Изображение не найдено'

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title, language='ru').exists():
                # Сохранение новости в базу данных с указанием русского языка
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_russian,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на русском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')



    def scrape_168am_russian_busniess(self):
        print("Скрапинг новостей на русском для категории 'Мировые новости'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.168.am/category/business-and-economics-ru'  # Замените на реальный URL
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='realated-item clearfix')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_russian = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='single-content')

            title_tag = data.find('h1', class_='single-title')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='single-content-wrapper')
            content = content_tag.text if content_tag else 'Контент не найден'

            image_tag = data.find('img', class_='attachment-full size-full wp-post-image')
            image = image_tag.get('src') if image_tag else 'Изображение не найдено'

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title, language='ru').exists():
                # Сохранение новости в базу данных с указанием русского языка
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_russian,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на русском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    def scrape_168am_russian_medic(self):
        print("Скрапинг новостей на русском для категории 'Мировые новости'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://ru.168.am/category/the-science-ru'  # Замените на реальный URL
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='realated-item clearfix')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_russian = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='single-content')

            title_tag = data.find('h1', class_='single-title')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='single-content-wrapper')
            content = content_tag.text if content_tag else 'Контент не найден'

            image_tag = data.find('img', class_='attachment-full size-full wp-post-image')
            image = image_tag.get('src') if image_tag else 'Изображение не найдено'

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title, language='ru').exists():
                # Сохранение новости в базу данных с указанием русского языка
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_russian,
                    date_scraped=timezone.now(),
                    language='ru'  # Указываем, что это новость на русском языке
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')