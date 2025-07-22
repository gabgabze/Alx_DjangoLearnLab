from django.urls import path
from .import views
#from django.contrib.auth import views as auth_views
urlpatterns = [
    path('books/', views.book_list, name='home'),
    path('detail/',views.LibraryDetailView.as_view(), name='detail' ),
    path('register/', views.register, name='register'),
    path('admin_view', views.admin_view, name='admin_view'),
    path('librarian/', views.librarian_view, name='librarian'),
    path('member/', views.member_view, name='member'),

    path('add_book/', views.add_book, name='add_book'),
    path('change_book/<int:pk>/', views.change_book, name='change_book'),
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),
]

