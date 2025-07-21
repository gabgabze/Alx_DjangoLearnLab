from django.urls import path
from .import views
#from django.contrib.auth import views as auth_views
urlpatterns = [
    path('books/', views.book_list, name='home'),
    path('detail/',views.LibraryDetailView.as_view(), name='detail' ),
    path('register/', views.register, name='register')
]

