import os
import asyncio
import time
from asgiref.sync import sync_to_async
from django.core.management.base import BaseCommand
from django.utils.timezone import make_aware, is_naive
from telethon.errors import FloodWaitError
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetHistoryRequest
from news.models import TelegramNews
from newsproject import settings

# Ваши учетные данные
api_id = '25029629'
api_hash = 'a6349b5e6cd7f76cb9f46217617b28c6'
phone = '+37493595863'
channel_username = 'https://t.me/+5bSS1J54NrNjOWYy'  # Ссылка на ваш канал

class Command(BaseCommand):
    help = 'Скрапинг новостей из Telegram'

    def handle(self, *args, **kwargs):
        asyncio.run(self.scrape_telegram_news())

    async def scrape_telegram_news(self):
        client = TelegramClient(phone, api_id, api_hash, request_retries=15, timeout=120)  # Увеличенное время ожидания
        await client.start()

        try:
            # Преобразуем ссылку в entity, чтобы клиент понял ее правильно
            channel = await client.get_entity(channel_username)

            messages = await client(GetHistoryRequest(
                peer=channel,
                limit=15,  # Ограничиваем количество сообщений
                offset_date=None,
                offset_id=0,
                max_id=0,
                min_id=0,
                add_offset=0,
                hash=0
            ))

            for message in messages.messages:
                if message.message:
                    text = message.message
                    date = message.date
                    media_file = None
                    media_type = None

                    # Проверяем, является ли дата наивной
                    if is_naive(date):
                        date = make_aware(date)

                    # Проверяем наличие медиа
                    if message.media:
                        try:
                            # Попробуем загрузить медиа до 5 раз в случае ошибки таймаута
                            for attempt in range(5):
                                try:
                                    if hasattr(message.media, 'photo'):
                                        media_path = await client.download_media(
                                            message.media,
                                            file=os.path.join(settings.MEDIA_ROOT, 'downloads', f'photo_{message.id}.jpg')
                                        )
                                        if media_path:
                                            media_file = media_path.replace(settings.MEDIA_ROOT, '').replace('\\', '/')
                                            media_type = 'Фото'
                                        break  # Если загрузка успешна, выходим из цикла попыток
                                    elif hasattr(message.media, 'document') and message.media.document.mime_type.startswith('video/'):
                                        media_path = await client.download_media(
                                            message.media,
                                            file=os.path.join(settings.MEDIA_ROOT, 'downloads', f'video_{message.id}.mp4')
                                        )
                                        if media_path:
                                            media_file = media_path.replace(settings.MEDIA_ROOT, '').replace('\\', '/')
                                            media_type = 'Видео'
                                        break
                                except (asyncio.TimeoutError, TimeoutError) as e:
                                    print(f"Ошибка загрузки медиа: {e}. Попытка {attempt + 1} из 5")
                                    if attempt < 4:
                                        time.sleep(20)  # Ждем 20 секунд перед повторной попыткой

                        except Exception as e:
                            self.stdout.write(self.style.ERROR(f"Ошибка при загрузке медиа: {e}"))

                    # Сохраняем только если есть текст и медиа файл
                    if media_file:
                        await sync_to_async(self.save_news_to_db)(text, date, media_type, media_file)

        except FloodWaitError as e:
            wait_time = e.seconds
            self.stdout.write(self.style.ERROR(f"Ошибка FloodWait. Нужно подождать {wait_time} секунд."))
            time.sleep(wait_time)
            # После ожидания можно попробовать снова
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Ошибка: {e}"))
        finally:
            await client.disconnect()

    def save_news_to_db(self, text, date, media_type, media_file):
        # Проверяем, существует ли уже новость в базе данных, чтобы избежать дубликатов
        if not TelegramNews.objects.filter(text=text, date_published=date).exists():
            TelegramNews.objects.create(
                text=text,
                date_published=date,
                media_type=media_type,
                media_file=media_file
            )
            self.stdout.write(self.style.SUCCESS(f'Новость "{text[:30]}..." успешно сохранена.'))
        else:
            self.stdout.write(self.style.WARNING(f'Новость "{text[:30]}..." уже существует.'))