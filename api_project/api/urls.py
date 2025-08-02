from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import BookViewSet

"""set the router"""
router = DefaultRouter()
router.register(r'my-books', BookViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
]
