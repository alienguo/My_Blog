from rest_framework import serializers
from apps.article.models import Article


class ArticleSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # title = serializers.CharField(allow_blank=True, max_length=100)
    # content = serializers.CharField(allow_blank=True)
    # create_time = serializers.DateTimeField()
    # update_time = serializers.DateTimeField()
    class Meta:
        model = Article
        fields = '__all__'
