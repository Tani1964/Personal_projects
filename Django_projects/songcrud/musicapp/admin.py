from django.contrib import admin
from .models import Artiste, Song, Lyric

# Register your models here.
admin.site.register(Artiste, Song, Lyric)