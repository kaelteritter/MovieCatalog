from unittest import TestCase
import unittest
from selenium import webdriver




class NewVisitorTest(TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_get_page(self):
        self.browser.get('http://127.0.0.1:8000')

        # Пользователь предпологает...
        self.assertIn('Movies', self.browser.title)
        self.fail('Закончить тест!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')