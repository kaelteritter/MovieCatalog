from django.contrib.auth import get_user_model
from django.test import Client, TestCase
from django.urls import reverse

from movies.forms import SingUpForm


User = get_user_model()

class SingUpFormTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass() 
        cls.existing_user = User.objects.create_user(username='testuser', 
                                                     email='test@example.com')
        
    def setUp(self):
        self.client = Client()
        
        
    def test_signup_form_creates_user(self):
        '''Тест: форма регистрации создает модель пользователя'''
        number_of_users_before = User.objects.count()
        data = {
            'email': 'alex@example.com',
            'password': '!changeMe',
            'password2': '!changeMe',
        }
        self.client.post(reverse('movies:signup'), data=data, follow=True)
        self.assertEqual(User.objects.count(), number_of_users_before + 1)