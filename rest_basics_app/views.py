from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . models import Article
from . serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics, mixins
from rest_framework.authentication import SessionAuthentication, TokenAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


# ModelViewSet will perform all functionalities
class ArticleViewSet(viewsets.ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

