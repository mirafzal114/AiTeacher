from django.test import TestCase

from django.test import TestCase, Client
from django.urls import reverse

class IELTSCheckingViewTest(TestCase):
    def test_ielts_checking_view_with_valid_data(self):
        client = Client()
        response = client.post(reverse('ielts_checking_view'), {'essay_text': 'Test essay text'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h1>your ielts writing score:</h1>')

    def test_ielts_checking_view_with_invalid_data(self):
        client = Client()
        response = client.post(reverse('ielts_checking_view'), {})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, '<h1>your ielts writing score:</h1>')

class DictionaryViewTest(TestCase):
    def test_dict_view_with_valid_data(self):
        client = Client()
        response = client.post(reverse('dict_view'), {'word': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, '<h2>Definition:</h2>')

    def test_dict_view_with_invalid_data(self):
        client = Client()
        response = client.post(reverse('dict_view'), {})
        self.assertEqual(response.status_code, 200)
        self.assertNotContains(response, '<h2>Definition:</h2>')


class AboutViewTest(TestCase):
    def test_about_view(self):
        client = Client()
        response = client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)



