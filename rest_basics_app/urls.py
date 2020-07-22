from django.contrib import admin
from django.urls import path, include
from . views import  ArticleAPIViews

urlpatterns = [
    path('article/', ArticleAPIViews.as_view(), name='Article_APIViews'),
    path('article/<int:id>/', ArticleDetail.as_view(), name='Article_detail'),
]

