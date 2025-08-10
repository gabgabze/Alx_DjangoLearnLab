from django.test import TestCase
from api.models import *

"""create a Book test case"""

class APITestCase(TestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")
        Book.objects.create("")
        Book.objects.create("")


class BookListTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")


class BookDetailTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")

class APITestCase(BookTestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")

class BookUpdateTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")
        Book.objects.create("")

class BookDeleteTestCase(APITestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")