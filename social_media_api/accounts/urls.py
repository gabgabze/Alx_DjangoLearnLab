from django.urls import path

from posts.views import PostViewSet
from .import views

url_patterns =[
    path('', views.home, name='home'),
    path('follow/<int:user_id>/', PostViewSet, name='follow'),
    path('unfollow/<int:user_id>/', PostViewSet, name='unfollow'),
]