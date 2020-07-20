from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from . models import Article
from . serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


# 'POST' method requires csrf token
@csrf_exempt
def article_list(request):
    if request.method=='GET':
        # first take Articles data from database
        articles = Article.objects.all()
        # convert it to serializers, we are reading quireset(multiple article) so put many=True 
        serializer = ArticleSerializer(articles, many=True) 
        # convert and return json data
        return JsonResponse(serializer.data, safe=False)

    elif request.method=='POST':
        # convert srting (json) data to dicts
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    except:
        return HttpResponse(status=404)

    if request.method=='GET':
        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)


    elif request.method=='PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)


    elif request.method=='DELETE':
        article.delete()
        return HttpResponse(status=204)





