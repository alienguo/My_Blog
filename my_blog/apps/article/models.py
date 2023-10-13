from django.db import models
from utils.models import BaseModel
from apps.user_info.models import User


class Article(BaseModel):
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='文章内容')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_article'
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章'

