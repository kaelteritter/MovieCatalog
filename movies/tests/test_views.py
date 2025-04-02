from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

from movies.views import home


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        '''
        тест: домашняя страница возвращает правильный html
        '''
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(
            html.startswith('<!DOCTYPE html>'), 
            "Проверьте, что возвращается страница HTML"
            )
        self.assertIn(
            '<title>Movies</title>', html,
            "Проверьте, что в заголовке главной страницы указано 'Movies'"
            )
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(
            response, 'index.html', 
            "Проверьте, что для главной страницы используется шаблон index.html"
            )
        
class SignUpTest(TestCase):
    def test_signup_page_returns_correct_html(self):
        '''
        тест: страница регистрации возвращает правильный html
        '''
        response = self.client.get('/signup/')
        html = response.content.decode('utf8')
        self.assertTrue(
            html.startswith('<!DOCTYPE html>'), 
            "Проверьте, что возвращается страница HTML"
            )
        self.assertIn(
            '<title>Sign Up</title>', html,
            "Проверьте, что в заголовке главной страницы указано 'Sign Up'"
            )
        self.assertTrue(html.endswith('</html>'))
        self.assertTemplateUsed(
            response, 'signup.html', 
            "Проверьте, что для главной страницы используется шаблон signup.html"
            )