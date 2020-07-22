from django.contrib import admin
from django.urls import path, include
from . views import article_list, article_detail

urlpatterns = [
    path('article/', article_list, name='article_list'),
    path('article/<int:id>/',article_detail, name='Article_detail'),
]

