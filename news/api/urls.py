from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('articles', api_views.ArticleListCreateAPIView.as_view(), name='article-list'),
    path('articles/<int:pk>', api_views.ArticleDetailAPIView.as_view(), name='article-detail'),

]