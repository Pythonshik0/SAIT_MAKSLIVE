from django.db import models
from datetime import datetime
from django.urls import reverse


class Image(models.Model):
    title = models.CharField(max_length=3031)
    image = models.ImageField(upload_to='images')


