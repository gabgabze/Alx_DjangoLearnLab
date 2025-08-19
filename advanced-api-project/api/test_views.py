from api.models import *
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework.test import APITestCase

"""create a Book test case"""
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

    def test_book(self):
        url = 'api/book-detail/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

class BookUpdateTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")

    def test_book(self):
        url = 'api/books/update'
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, dict)

class BookDeleteTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")



"""create a test case db"""

class DBTestCase(APITestCase):
    def setUp(self):
        """create a test case db"""
        self.user = User.objects.create_user(
            username='testuser',
            email='<EMAIL>',
            password='<PASSWORD>'
        )
    def test_db(self):
        """login user using django database"""
        login_success = self.client.login(
            username='testuser',
            password='<PASSWORD>'
        )
        self.assertTrue(login_success)

        # Now make authenticated request
        response = self.client.get('api/db/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)