from django.contrib.auth import get_user_model
from django.db import models
from django.test import TestCase

from movies.models import Genre, Movie, Review


User = get_user_model()


class UserModelTest(TestCase):
    def test_movie_model_has_fields(self):
        excepted_fields = {
            'id',
            'username',
            'password',
            'email'
        }

        current_fields = [field.name for field in User._meta.get_fields()]
        for field in excepted_fields:
            with self.subTest(field=field):
                self.assertIn(
                    field, current_fields,
                    f'Проверьте наличие поля {field} у модели Movie'
                            )

class MovieModelTest(TestCase):   
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
            with self.subTest(field=field):
                self.assertIn(
                    field, current_fields,
                    f'Проверьте наличие поля {field} у модели Movie'
                            )

    def test_movie_fields_have_right_types(self):
        excepted_fields = {
            'title': models.CharField,
            'description': models.TextField,
            'release_year': models.IntegerField,
            'genre': models.ManyToManyField,
            'rating': models.DecimalField,
        }

        for name, field_type in excepted_fields.items():
            field = Movie._meta.get_field(name)
            self.assertIsInstance(field, field_type, f'Поле {name} имеет неверный тип')

    def test_movie_field_required_params(self):
        fields_param_map = {
            'title': {
                'unique': True,
                'blank': False,
                'null': False,
                'max_length': 255,
            },
            'description': {
                'unique': False,
                'blank': True,
                'null': True,
                'max_length': 4095,
            },
            'release_year': {
                'unique': False,
                'blank': True,
                'null': True,
            },
            'genre': {
                'unique': False,
                'blank': True,
            },
            'rating': {
                'unique': False,
                'blank': False,
                'null': False,
                'default': 0,
            },
        }

        for existing_field in Movie._meta.get_fields():
            with self.subTest(existing_field=existing_field):
                attrs = fields_param_map.get(existing_field.name)
                if attrs:
                    for param, value in attrs.items():
                        self.assertEqual(
                            getattr(existing_field, param), value,
                            f'Поле {existing_field.name} имеет параметр {param}: '
                            f'{getattr(existing_field, param)}, а должен: {value}'
                            )


class GenreModelTest(TestCase):
    def test_genre_model_has_fields(self):
        excepted_fields = {
            'id',
            'title',
        }

        current_fields = [field.name for field in Genre._meta.get_fields()]
        for field in excepted_fields:
            with self.subTest(field=field):
                self.assertIn(
                    field, current_fields,
                    f'Проверьте наличие поля {field} у модели Genre'
                            )
                
    def test_genre_fields_have_right_types(self):
        excepted_fields = {
            'title': models.CharField,
        }

        for name, field_type in excepted_fields.items():
            field = Genre._meta.get_field(name)
            self.assertIsInstance(field, field_type, f'Поле {name} имеет неверный тип')

    def test_genre_field_required_params(self):
        fields_param_map = {
            'title': {
                'unique': True,
                'blank': False,
                'null': False,
                'max_length': 255,
            }
        }

        for existing_field in Genre._meta.get_fields():
            with self.subTest(existing_field=existing_field):
                attrs = fields_param_map.get(existing_field.name)
                if attrs:
                    for param, value in attrs.items():
                        self.assertEqual(
                            getattr(existing_field, param), value,
                            f'Поле {existing_field.name} имеет параметр {param}: '
                            f'{getattr(existing_field, param)}, а должен: {value}'
                            )
                        
                        
class ReviewModelTest(TestCase):
    def test_review_model_has_fields(self):
        excepted_fields = {
            'id',
            'author',
            'text',
            'movie',
        }

        current_fields = [field.name for field in Review._meta.get_fields()]
        for field in excepted_fields:
            with self.subTest(field=field):
                self.assertIn(
                    field, current_fields,
                    f'Проверьте наличие поля {field} у модели Genre'
                            )
                
    def test_review_fields_have_right_types(self):
        excepted_fields = {
            'movie': models.ForeignKey,
            'author': models.ForeignKey,
            'text': models.TextField,
        }

        for name, field_type in excepted_fields.items():
            field = Review._meta.get_field(name)
            self.assertIsInstance(field, field_type, f'Поле {name} имеет неверный тип')

    def test_review_field_required_params(self):
        fields_param_map = {
            'author': {
                'blank': False,
                'null': False,
            },
            'movie': {
                'blank': False,
                'null': False,
            },
            'text': {
                'unique': False,
                'blank': False,
                'null': False,
                'max_length': 4095,
            },
        }

        for existing_field in Review._meta.get_fields():
            with self.subTest(existing_field=existing_field):
                attrs = fields_param_map.get(existing_field.name)
                if attrs:
                    for param, value in attrs.items():
                        self.assertEqual(
                            getattr(existing_field, param), value,
                            f'Поле {existing_field.name} имеет параметр {param}: '
                            f'{getattr(existing_field, param)}, а должен: {value}'
                            )
                        
