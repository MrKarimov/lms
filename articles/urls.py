from django.urls import path
from .views import ArticlesListView, ArticleDetailView, ArticleDeleteView, ArticleUpdateView ,ArticleCreateView

urlpatterns = [
    
    path('', ArticlesListView.as_view(), name='article_list'),
    path('<int:pk>/edit/', ArticleUpdateView.as_view(), name = "article_edit"),
    path('<int:pk>/delete/', ArticleDeleteView.as_view(), name = "article_delete"),
    path('<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
    path('create/', ArticleCreateView.as_view(), name = 'article_create'),
]
