from django.urls import path
from relationship_app import views

url_patterns =[
    path('books/', views.book_list, name='home'),
    path('detail/', views.BookDetail.as_view(), name='detail' ),
]
