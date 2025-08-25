from django.urls import path
from accounts.urls import *
from .import views

url_patterns =[
    path('/feed',views.PostUserViewSet.as_view(), name='feed'),
]