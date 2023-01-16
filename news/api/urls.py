from django.urls import path
from news.api import views as api_views

urlpatterns = [
    path('articles', api_views.article_list_create_api_view, name='article-list'),
    path('articles/<int:pk>', api_views.article_detail_api_view, name='article-detail'),

]