from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

"""set the router"""
router = DefaultRouter()
  #  path('', BookList.as_view(), name='book-list'),
router.register('books', BookViewSet.as_view(), basename='book_all'),
urlpatterns = router.urls
