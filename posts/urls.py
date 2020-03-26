from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('posts/', views.posts_list, name="posts_list"),
    path('posts/create/', views.post_create, name="create"),
    path('posts/<post_id>/', views.post_detail, name="detail"),
    path('posts/<post_id>/update/', views.post_update, name="update"),
    path('posts/<post_id>/delete/', views.post_delete, name="delete"),
]
