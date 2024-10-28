from django.contrib import admin
from .models import News, Category, ContactMessage, TelegramNews

# Register your models here.

admin.site.register(News)
admin.site.register(Category)
admin.site.register(ContactMessage)
admin.site.register(TelegramNews)