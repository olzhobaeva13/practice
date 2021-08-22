from django.urls import path
from .views import posts_list_view

urlpatterns = [
    path('posts/', posts_list_view, name='post_list_url')
]