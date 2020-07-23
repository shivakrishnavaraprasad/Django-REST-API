from django.contrib import admin
from django.urls import path, include
from . views import ArticleDetail, ArticleAPIViews, GenericApiView

urlpatterns = [
    path('article/', ArticleAPIViews.as_view(), name='Article_APIViews'),
    path('article/<int:id>/', ArticleAPIViews.as_view(), name='Article_detail'),
    
    # for get | post
    path('generic/article/', GenericApiView.as_view(), name='generic_views'), 
    # for put | delete
    path('generic/article/<int:id>/', GenericApiView.as_view(), name='generic_views'),
]

