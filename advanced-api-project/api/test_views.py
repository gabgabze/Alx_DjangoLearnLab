from django.test import TestCase
from api.models import *

"""create a Book test case"""

class BookTestCase(TestCase):
    def setUp(self):
        Book.objects.create("")
        Book.objects.create("")
        Book.objects.create("")
        Book.objects.create("")


class BookListTestCase(BookTestCase):
    def setUp(self):
        Book.objects.create("")