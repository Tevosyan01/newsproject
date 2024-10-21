import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint  # Для генерации случайной задержки
from django.core.management import BaseCommand
from news.models import News, Category
from django.utils import timezone


class Command(BaseCommand):
    help = 'Скрапинг новостей для категорий "Мировые новости", "Спорт" и "Армения" с задержками для избежания блокировки'

    def handle(self, *args, **kwargs):
        self.scrape_168am_faces()
        self.scrape_168am_press()
        self.scrape_168am_sports()
        self.scrape_aravot_news_education()
        self.scrape_aravot_news_society()
        self.scrape_aravot_news_politics()
        self.scrape_aravot_news_rights()
        self.scrape_world_news()
        self.scrape_sport_news()
        self.scrape_armenia_news()
        self.scrape_more_news()


    def scrape_168am_faces(self):
        print("Скрапинг новостей для категории 'ԱՇԽԱՐՀ'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://168.am/section/faces'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='realated-item clearfix')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_sports = Category.objects.get_or_create(name='ԱՇԽԱՐՀ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='single-content')

            # Извлечение данных с проверками
            title_tag = data.find('h1', class_='single-title')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='single-content-wrapper')
            content = content_tag.text if content_tag else 'Контент не найден'

            image_tag = data.find('img', class_='attachment-full size-full wp-post-image')
            image = image_tag.get('src') if image_tag else 'Изображение не найдено'

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title).exists():
                # Сохранение новости в базу данных
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_sports,
                    date_scraped=timezone.now()
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    def scrape_168am_press(self):
        print("Скрапинг новостей для категории 'ԱՎԵԼԻՆ'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://168.am/section/press-am'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='realated-item clearfix')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_sports = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='single-content')

            # Извлечение данных с проверками
            title_tag = data.find('h1', class_='single-title')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='single-content-wrapper')
            content = content_tag.text if content_tag else 'Контент не найден'

            image_tag = data.find('img', class_='attachment-full size-full wp-post-image')
            image = image_tag.get('src') if image_tag else 'Изображение не найдено'

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title).exists():
                # Сохранение новости в базу данных
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_sports,
                    date_scraped=timezone.now()
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    def scrape_168am_sports(self):
        print("Скрапинг новостей для категории 'ՍՊՈՐՏ'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://168.am/section/sports-am'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='realated-item clearfix')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_sports = Category.objects.get_or_create(name='ՍՊՈՐՏ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='single-content')

            # Извлечение данных с проверками
            title_tag = data.find('h1', class_='single-title')
            title = title_tag.text if title_tag else 'Заголовок не найден'

            content_tag = data.find('div', class_='single-content-wrapper')
            content = content_tag.text if content_tag else 'Контент не найден'

            image_tag = data.find('img', class_='attachment-full size-full wp-post-image')
            image = image_tag.get('src') if image_tag else 'Изображение не найдено'

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title).exists():
                # Сохранение новости в базу данных
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_sports,
                    date_scraped=timezone.now()
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')

    def scrape_aravot_news_education(self):
        print("Скрапинг новостей для категории 'ՀԱՅԱՍՏԱՆ'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://www.aravot.am/category/news/education/'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_politics = Category.objects.get_or_create(name='ՀԱՅԱՍՏԱՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            # Извлечение данных
            title = data.find('h1', class_='display-7').text
            content = data.find('div', class_='post_content').text
            image = data.find('img', class_='rounded w-100 wp-post-image').get('src')

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title).exists():
                # Сохранение новости в базу данных
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_politics,
                    date_scraped=timezone.now()
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')

    def scrape_aravot_news_society(self):
        print("Скрапинг новостей для категории 'ԱՎԵԼԻՆ'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://www.aravot.am/category/news/society/'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_politics = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            # Извлечение данных
            title = data.find('h1', class_='display-7').text
            content = data.find('div', class_='post_content').text
            image = data.find('img', class_='rounded w-100 wp-post-image').get('src')

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title).exists():
                # Сохранение новости в базу данных
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_politics,
                    date_scraped=timezone.now()
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')

    def scrape_aravot_news_politics(self):
        print("Скрапинг новостей для категории 'ՀԱՅԱՍՏԱՆ'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://www.aravot.am/category/news/politics/'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_politics = Category.objects.get_or_create(name='ՀԱՅԱՍՏԱՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            # Извлечение данных
            title = data.find('h1', class_='display-7').text
            content = data.find('div', class_='post_content').text
            image = data.find('img', class_='rounded w-100 wp-post-image').get('src')

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title).exists():
                # Сохранение новости в базу данных
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_politics,
                    date_scraped=timezone.now()
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    def scrape_aravot_news_rights(self):
        print("Скрапинг новостей для категории 'ՀԱՅԱՍՏԱՆ'")

        list_news_urls = []

        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        }

        url = 'https://www.aravot.am/category/news/rights/'

        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')

        # Найти все ссылки на новости
        data = soup.find_all('div', class_='col-3')
        for i in data:
            news_url = i.find('a').get('href')
            list_news_urls.append(news_url)

        # Категория для новостей
        category_politics = Category.objects.get_or_create(name='ՀԱՅԱՍՏԱՆ')[0]

        # Парсим каждую новость и сохраняем в базу данных
        for news_url in list_news_urls:
            sleep(1)
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='col-lg-6 mb-5 single-wraper')

            # Извлечение данных
            title = data.find('h1', class_='display-7').text
            content = data.find('div', class_='post_content').text
            image = data.find('img', class_='rounded w-100 wp-post-image').get('src')

            # Проверка на дубликаты по заголовку
            if not News.objects.filter(title=title).exists():
                # Сохранение новости в базу данных
                News.objects.create(
                    title=title,
                    content=content,
                    image=image,
                    category=category_politics,
                    date_scraped=timezone.now()
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует.')


    # Скрапинг для категории "Мир"
    def scrape_world_news(self):
        print("Скрапинг новостей для категории 'Мир'")
        list_news_urls = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

        for count in range(1, 3):  # Например, собираем 2 страницы
            sleep(1)
            url = f'https://shamshyan.com/hy/category/world?page={count}'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find_all('div', class_='category-card bg-gray-100 rounded-lg')

            for i in data:
                news_url = i.find('a').get('href')
                list_news_urls.append(news_url)

        category_world = Category.objects.get_or_create(name='ԱՇԽԱՐՀ')[0]  # Категория "Мир"
        self.scrape_and_save_news(list_news_urls, category_world)

    def scrape_more_news(self):
        print("Скрапинг новостей для категории 'ԱՎԵԼԻՆ'")
        list_news_urls = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

        for count in range(1, 3):  # Например, собираем 2 страницы
            sleep(1)
            url = f'https://shamshyan.com/hy/category/gagik-shamshyan?page={count}'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find_all('div', class_='category-card bg-gray-100 rounded-lg')

            for i in data:
                news_url = i.find('a').get('href')
                list_news_urls.append(news_url)

        category_more = Category.objects.get_or_create(name='ԱՎԵԼԻՆ')[0]  # Категория "ԱՎԵԼԻՆ"
        self.scrape_and_save_news(list_news_urls, category_more)

    # Скрапинг для категории "Спорт"
    def scrape_sport_news(self):
        print("Скрапинг новостей для категории 'Спорт'")
        list_news_urls = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

        for count in range(1, 3):  # Например, собираем 2 страницы
            sleep(1)
            url = f'https://shamshyan.com/hy/category/sport?page={count}'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find_all('div', class_='category-card bg-gray-100 rounded-lg')

            for i in data:
                news_url = i.find('a').get('href')
                list_news_urls.append(news_url)

        category_sport = Category.objects.get_or_create(name='ՍՊՈՐՏ')[0]  # Категория "Спорт"
        self.scrape_and_save_news(list_news_urls, category_sport)

    # Скрапинг для категории "Армения"
    def scrape_armenia_news(self):
        print("Скрапинг новостей для категории 'Армения'")
        list_news_urls = []
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}

        for count in range(1, 3):  # Например, собираем 2 страницы
            sleep(1)
            url = f'https://shamshyan.com/hy/category/armenia?page={count}'
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')
            data = soup.find_all('div', class_='category-card bg-gray-100 rounded-lg')

            for i in data:
                news_url = i.find('a').get('href')
                list_news_urls.append(news_url)

        category_armenia = Category.objects.get_or_create(name='ՀԱՅԱՍՏԱՆ')[0]  # Категория "Армения"
        self.scrape_and_save_news(list_news_urls, category_armenia)

    # Универсальная функция для сохранения новостей в базе данных
    def scrape_and_save_news(self, news_urls, category):
        headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
        for news_url in news_urls:
            sleep(3)  # Задержка  3  секунд
            response = requests.get(news_url, headers=headers)
            soup = BeautifulSoup(response.text, 'lxml')

            data = soup.find('div', class_='flex flex-wrap md:flex-nowrap space-x-5 space-y-5 global-div')

            title = data.find('h1', class_='py-[10px] xfont-extrabold article-title').text if data.find('h1',
                                                                                                        class_='py-[10px] xfont-extrabold article-title') else 'Заголовок не найден'
            content = data.find('div', class_='text-side text-black dark:text-white mt-[20px]').text if data.find('div',
                                                                                                                  class_='text-side text-black dark:text-white mt-[20px]') else 'Контент не найден'

            image_div = data.find('div',
                                  class_='w-full article-card p-5 bg-white rounded-lg shadow-md bg-gray-800 border-gray-700')
            if image_div:
                image_style = image_div.get('style')
                if image_style:
                    image_url = image_style.replace('background-image: url', '').strip('()"')
                    full_image_url = 'https://shamshyan.com' + image_url if image_url.startswith('/') else image_url
                else:
                    full_image_url = 'Изображение не найдено'
            else:
                full_image_url = 'Изображение не найдено'

            # Проверка на наличие новости в базе данных
            if not News.objects.filter(title=title).exists():
                News.objects.create(
                    title=title,
                    content=content,
                    image=full_image_url,
                    category=category,
                    date_scraped=timezone.now()
                )
                print(f'Новость "{title}" успешно сохранена.')
            else:
                print(f'Новость "{title}" уже существует в базе данных.')



