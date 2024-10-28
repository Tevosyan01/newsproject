from django.db import models
import random
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name



def random_views():
    return random.randint(150, 500)

class News(models.Model):
    LANGUAGES = [
        ('hy', 'Армянский'),
        ('ru', 'Русский'),
        ('en', 'Английский'),
    ]

    title = models.CharField(max_length=255)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_image/', blank=True, null=True)
    views = models.PositiveIntegerField(default=random_views)
    date_scraped = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=2, choices=LANGUAGES, default='hy')
    urllib = models.URLField(null=True, blank=True)


    def __str__(self):
        return f'{self.title} ({self.get_language_display()})'


class TelegramNews(models.Model):
    text = models.TextField()
    date_published = models.DateTimeField()
    media_type = models.CharField(max_length=20, null=True, blank=True)
    media_file = models.FileField(upload_to='telegram_media/', null=True, blank=True)

    def __str__(self):
        # Изменение метода __str__ для предотвращения ошибок
        if isinstance(self.date_published, str):
            return f"Telegram News on {self.date_published}"
        elif isinstance(self.date_published, datetime):
            return f"Telegram News from {self.date_published.strftime('%Y-%m-%d %H:%M')}"
        else:
            return "Telegram News (unknown date)"



class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сообщение от {self.name} ({self.email})"