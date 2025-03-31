from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Genre(models.Model):
    title = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f'Genre: {self.title}'
    
    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Movie(models.Model):
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    description = models.TextField(blank=True, null=True, max_length=4095)
    title = models.CharField(max_length=255, unique=True)
    release_year = models.IntegerField(blank=True, null=True)
    genre = models.ManyToManyField(
        Genre, 
        blank=True
        )
    
    def __str__(self):
        return f'Movie: {self.title}'
    
    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'


class Review(models.Model):
    text = models.TextField(max_length=4095)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return  f'Review: Author: {self.author}; Movie: {self.movie.title}'
    
    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'