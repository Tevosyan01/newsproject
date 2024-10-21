from django.db import models
import random

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

    def __str__(self):
        return f'{self.title} ({self.get_language_display()})'



class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сообщение от {self.name} ({self.email})"