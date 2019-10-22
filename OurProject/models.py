from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.

class Topic_of_shirts(models.Model):
    topic = models.CharField(max_length = 30)

class Tag_for_shirts(models.Model):
    tag = models.CharField(max_length = 50)

class User_settings(models.Model):
    LANGUAGE_CHOICES  = (
        ('EN', 'English'),
        ('RU', 'Russian'),

    )
    COLOR_OF_INTERFACE_CHOICES  = (
        ('L', 'Light'),
        ('D', 'Dark'),

    )
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    language_intarface = models.CharField(max_length = 2, choices = LANGUAGE_CHOICES)
    color_of_intarface = models.CharField(max_length = 1, choices = COLOR_OF_INTERFACE_CHOICES)

class Shirt(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    topic_id = models.ForeignKey(Topic_of_shirts, on_delete=models.CASCADE)
    tag_id = models.ForeignKey(Tag_for_shirts, on_delete=models.CASCADE)
    name_of_shirt = models.CharField(max_length = 30)
    description_of_shirt = models.TextField()
    created_time = models.DateTimeField(default=timezone.now)
    picture_of_shirt = models.CharField(max_length = 200)

class Comment_of_shirt(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shirt_id = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    comment_for_shirt = models.TextField()

class Rating_of_shirt(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    shirt_id = models.ForeignKey(Shirt, on_delete=models.CASCADE)
    rating_for_shirt = models.CharField(max_length = 2)
