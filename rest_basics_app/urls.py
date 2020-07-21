from django.contrib import admin
from django.urls import path, include
from . views import article_list, article_detail, ArticleAPIViews

urlpatterns = [
    path('article/', ArticleAPIViews.as_view(), name='Article_APIViews'),
    path('article/<int:id>/', ArticleAPIViews.as_view(), name='Article_detail'),
]

