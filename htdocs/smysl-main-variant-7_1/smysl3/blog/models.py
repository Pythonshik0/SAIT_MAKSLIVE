from django.db import models
from datetime import datetime
from django.urls import reverse
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=999999)
    full_text = models.CharField(max_length=999999)
    summary = models.CharField(max_length=999999)
    categery = models.CharField(max_length=9999)
    puddate = models.DateTimeField()
    slug = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.slug

    # функция, которая ниже говорит: дай мне переменную с именем article_page
    def get_absolute_url(self):
        return reverse('article_page', kwargs={'slug': self.slug})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Additional(models.Model):
    title = models.CharField(max_length=999999)
    full_text = models.CharField(max_length=999999)
    categories = models.CharField(max_length=9999)


class Item(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField(max_length=500)


class Comment(models.Model):
    name = models.CharField(max_length=80)
    body = models.TextField()
    email = models.EmailField()


