from django.urls import path,include
from rest_framework.routers import DefaultRouter

from notifications.views import NotificationViewSet

notification_router = DefaultRouter()
notification_router.register(r'notifications', NotificationViewSet, basename='notifications')
urlpatterns = [
    path('notifications/', include(notification_router.urls)),
]