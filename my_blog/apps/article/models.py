from django.db import models
from utils.models import BaseModel


class Article(BaseModel):
    title = models.CharField(max_length=100, verbose_name='标题')
    content = models.TextField(verbose_name='文章内容')

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'tb_article'
        verbose_name = '博客文章'
        verbose_name_plural = '博客文章'

