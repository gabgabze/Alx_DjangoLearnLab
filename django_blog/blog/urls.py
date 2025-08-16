from django.urls import path
from .import views
from django.views import generic

urlpatterns =[
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('post/', views.blog, name='blog'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post/new'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

]