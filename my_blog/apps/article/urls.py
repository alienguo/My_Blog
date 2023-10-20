from django.urls import path, include
from apps.article import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'articles', views.ArticleViewSet)
router.register(r'category', views.CategoryViewSet)
urlpatterns = [
    path('', include(router.urls))
    # path('articles/', views.ArticleListAPIView.as_view()),
    # path('articles/<int:pk>/', views.ArticleDetailRUDAPIView.as_view(), name='detail'),
]
