from django.urls import path
from .import views
from django.views import generic

urlpatterns =[
    path('login/', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),

    # crud operation CBV paths

    path('post/', views.PostListView.as_view(), name='posts'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<int:pk>/update/', views.PostUpdateView.as_view(), name='post/new/'),
    path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post_delete'),

    # crud operation  CBV for comment
    path('post/<int:pk>/comments/new', views.CommentCreateView.as_view(), name='comments'),
    #path('post/<int:pk>/like/', views.LikePostView.as_view(), name='like'),
    #path('post/<int:pk>/dislike/', views.DislikePostView.as_view(), name='dislike'),
    path('comment/<int:pk>/delete/', views.CommentDeleteView.as_view(), name='comment_delete'),
    path('comment/<int:pk>/update', views.CommentUpdateView.as_view(), name='comments/new/'),

]