from django.urls import path
from accounts.urls import *
from .import views

url_patterns =[
    path('feed',views.PostUserViewSet.as_view(), name='feed/'),
    path('<int:pk>/like/',views.LikeViewSet,name='like/'),
    path('<int:pk>/unlike/',views.UnlikeViewSet,name='unlike/'),
]