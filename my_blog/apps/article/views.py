from django.shortcuts import render
from apps.article.models import Article
from apps.article.serializers import ArticleSerializer
from rest_framework.views import APIView
from rest_framework import mixins, viewsets
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from apps.article.models import Category
from apps.article.serializers import CategorySerializer, CategoryDetailSerializer


# class ArticleListAPIView(APIView):
#
#     permission_classes = [IsAuthenticatedOrReadOnly]
#
#     def get(self, request):
#         articles = Article.objects.all()
#         serializer = ArticleSerializer(articles, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class ArticleDetailAPIView(APIView):
#
#     def get(self, request, pk):
#         article = Article.objects.get(id=pk)
#         serializer = ArticleSerializer(article)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         article = Article.objects.get(id=pk)
#         serializer = ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         article = Article.objects.get(id=pk)
#         article.delete()
#         # 删除成功后返回204
#         return Response(status=status.HTTP_204_NO_CONTENT)


# class ArticleDetailGenericAPIView(mixins.RetrieveModelMixin,
#                                   mixins.UpdateModelMixin,
#                                   mixins.DestroyModelMixin,
#                                   GenericAPIView):
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#
#     def get(self, request, pk):
#         return self.retrieve(request)
#
#     def put(self, request, pk):
#         return self.update(request)
#
#     def delete(self, request, pk):
#         return self.destroy(request)


# class ArticleDetailRUDAPIView(RetrieveUpdateDestroyAPIView):
#
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer
#     permission_classes = [IsAuthenticatedOrReadOnly]

class ArticleViewSet(viewsets.ModelViewSet):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # 实现文章标题和内容的模糊搜索
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']
    # filterset_fields = ['author__username', 'title']


class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'list':
            return CategorySerializer
        else:
            return CategoryDetailSerializer
