from django.db import models

# Create your models here.

class Artiste(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateField(auto_now_add=True)
    likes = models.IntegerFeild
    artiste_id = models.IntegerField()

class Lyric(models.Model):
    content = models.TextField()
    song_id = models.IntegerField()