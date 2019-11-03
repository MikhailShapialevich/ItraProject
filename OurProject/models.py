from django.db import models
from django.conf import settings
from django.utils import timezone
from django.urls import reverse

# Create your models here.

class Topic_of_shirts(models.Model):
    topic = models.CharField(max_length = 30)
    def __str__(self):
        return self.topic

class Tag_for_shirts(models.Model):
    tag = models.CharField(max_length = 50)
    def __str__(self):
        return self.tag
class User_settings(models.Model):
    LANGUAGE_CHOICES  = (
        ('EN', 'English'),
        ('RU', 'Russian'),

    )
    COLOR_OF_INTERFACE_CHOICES  = (
        ('L', 'Light'),
        ('D', 'Dark'),

    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language_intarface = models.CharField(max_length = 2, choices = LANGUAGE_CHOICES)
    color_of_intarface = models.CharField(max_length = 1, choices = COLOR_OF_INTERFACE_CHOICES)

class Shirt(models.Model):
    image_height = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    image_width = models.PositiveIntegerField(null=True, blank=True, editable=False, default="100")
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic_of_shirts, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag_for_shirts, on_delete=models.CASCADE)
    name_of_shirt = models.CharField(max_length = 30)
    description_of_shirt = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    picture_of_shirt = models.ImageField(upload_to='images', height_field='image_height', width_field='image_width', blank=True)
    def __str__(self):
        return self.name_of_shirt
    @property
    def photo_url(self):
        if self.picture_of_shirt and hasattr(self.picture_of_shirt, 'url'):
            return self.picture_of_shirt.url
class Comment_of_shirt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    comment_for_shirt = models.TextField()

class Rating_of_shirt(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shirt = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    rating_for_shirt = models.CharField(max_length = 2)
