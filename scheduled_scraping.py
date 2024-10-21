import os
import django
from apscheduler.schedulers.blocking import BlockingScheduler
from django.core.management import call_command
from datetime import datetime
import pytz

# Настраиваем Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'newsproject.settings')  # Убедись, что здесь правильно указан твой проект
django.setup()

# Создаем планировщик задач
scheduler = BlockingScheduler()

# Функция для скрапинга новостей
def scrape_news():
    print(f"[{datetime.now()}] Запуск скрапинга новостей.")
    call_command('scrape_news_ru')  # Вызов команды Django для скра��инга новостей на русском языке
    call_command('scrape_news_en')
    call_command('scrape_news')  # Вызов команды Django для скрапинга новостей


# Настраиваем временную зону
timezone = pytz.timezone('Europe/Moscow')

# Добавляем задачу: запуск каждые 5 минут
scheduler.add_job(scrape_news, 'interval', minutes=1, timezone=timezone)

# Сообщение о старте планировщика
print("Планировщик запущен. Ждём выполнения задач...")

# Запускаем планировщик
scheduler.start()

