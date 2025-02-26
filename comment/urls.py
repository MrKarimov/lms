from django.urls import path
from .views import article_detail

urlpatterns = [
    path('articles/<int:pk>/', article_detail, name='article_detail'),
]
