from django.contrib import admin
from django.urls import path, include
from . views import GenericApiView

urlpatterns = [    

    path('generic/article/<int:id>/', GenericApiView.as_view(), name='generic_views'),
]

