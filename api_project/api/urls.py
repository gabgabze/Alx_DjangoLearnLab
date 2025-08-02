from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token


"""set the router"""
router = DefaultRouter()
router.register(r'my-books', BookViewSet)
urlpatterns = [
    path('api/', include(router.urls)),
    path('api/auth/', obtain_auth_token),
]
