from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from movies.views import home


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page(self):
        '''
        Контроллер для '/' называется home
        '''
        found = resolve('/')
        self.assertEqual(found.func.__name__, 'home')

    def test_home_page_returns_correct_html(self):
        '''
        тест: домашняя страница возвращает правильный html
        '''
        request = HttpRequest()
        response = home(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>Movies</title>', html)
        self.assertTrue(html.endswith('</html>'))