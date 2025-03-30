from django.db import models
from django.test import TestCase

from movies.models import Movie


class UserModelTest(TestCase):
    def setUp(self):
        return super().setUp()
    
    def test_movie_model_has_fields(self):
        excepted_fields = {
            'id',
            'title',
            'description',
            'release_year',
            'genre',
            'rating',
        }

        current_fields = [field.name for field in Movie._meta.get_fields()]
        for field in excepted_fields:
            self.assertIn(
                field, current_fields,
                f'Проверьте наличие поля {field} у модели Movie'
                          )

    def test_movie_fields_have_right_types(self):
        excepted_fields = {
            'title': models.CharField,
            'description': models.TextField,
            'release_year': models.IntegerField,
            'genre': models.ForeignKey,
            'rating': models.DecimalField,
        }

        for name, field_type in excepted_fields.items():
            field = Movie._meta.get_field(name)
            self.assertIsInstance(field, field_type, f'Поле {name} имеет неверный тип')
