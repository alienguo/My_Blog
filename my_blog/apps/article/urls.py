from django.urls import path
from apps.article import views

urlpatterns = [
    path('articles/', views.ArticleListAPIView.as_view()),
    path('articles/<int:pk>/', views.ArticleDetailRUDAPIView.as_view(), name='detail'),
]
