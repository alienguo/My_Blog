from django.urls import path
from apps.article import views

urlpatterns = [
    path('articles/', views.ArticleAPIView.as_view()),
]
