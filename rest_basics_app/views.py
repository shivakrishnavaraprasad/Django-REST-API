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
from rest_framework import generics
from rest_framework import mixins


################### generic api views #################################
class GenericApiView(generics.GenericAPIView, mixins.ListModelMixin,
                                              mixins.CreateModelMixin, 
                                              mixins.UpdateModelMixin,
                                              mixins.RetrieveModelMixin,
                                              mixins.DestroyModelMixin,):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):
        return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    
    def delete(self, request, id=None):
        return self.destroy(request, id)
