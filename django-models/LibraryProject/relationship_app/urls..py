from django.urls import path
from relationship_app import views,BookDetail

url_patterns =[
    path('books/', views.book_list, name='home'),
    path('detail', BookDetail.as_view(), name='detail' ),
]
