from django.db import models
from django.conf import settings

# Create your models here.

class Genre(models.Model):
    name = models.CharField(max_length=100)

class Movie(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=100)
    overview = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    language = models.CharField(max_length=100)
    poster_path = models.CharField(max_length=200)
    popularity = models.FloatField()
    vote_average = models.FloatField()
    release_date = models.DateField()
    adult = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    video_url = models.CharField(max_length=100, null=True, blank=True)
    
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_reviews')

class Moviecup(models.Model) :
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='moviecup')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

