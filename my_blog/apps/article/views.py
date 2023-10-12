from django.shortcuts import render
from apps.article.models import Article
from apps.article.serializers import ArticleSerializer
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response


class ArticleAPIView(APIView):

    def get(self, request):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)



