from django.test import TestCase
from api.models import *
from rest_framework import status

"""create a Book test case"""

class APITestCase(TestCase):
    def setUp(self):
        Book.objects.create("")

class BookListTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")

    # create a test endpoint method
    def test_book(self):
        url = 'api/book-list/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list)


class BookDetailTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")


    def test_book(self):
        url = 'api/book-detail/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookUpdateTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")

    def test_book(self):
        url = 'api/books/update'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

class BookDeleteTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")