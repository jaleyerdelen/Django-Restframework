from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('authors', api_views.JournalistListCreateAPIView.as_view(), name='author-list'),
    path('articles', api_views.ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', api_views.ArticleDetailAPIView.as_view(), name='article-detail'),

]