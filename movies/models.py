from django.db import models


class Genre(models.Model):
    pass


class Movie(models.Model):
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()
    title = models.CharField(max_length=128)
    release_year = models.IntegerField()
    genre = models.ForeignKey(Genre, on_delete=models.PROTECT)
