from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class News(models.Model):
    title = models.CharField(max_length=255,)
    content = models.TextField()
    date_published = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='news_image/', blank=True, null=True)
    views = models.PositiveIntegerField(default=0)
    date_scraped = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Сообщение от {self.name} ({self.email})"