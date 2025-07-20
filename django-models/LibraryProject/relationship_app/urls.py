from django.urls import path
from .import views
from django.contrib.auth import views as auth_views
url_patterns =[
    path('books/', views.book_list, name='home'),
    path('detail/',views.LibraryDetailView.as_view(), name='detail' ),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register')
]
