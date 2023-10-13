from rest_framework import serializers
from apps.article.models import Article
from apps.user_info.serializers import UserSerializer


# class ArticleSerializer(serializers.ModelSerializer):
#     # id = serializers.IntegerField(read_only=True)
#     # title = serializers.CharField(allow_blank=True, max_length=100)
#     content = serializers.CharField(required=False)
#     # create_time = serializers.DateTimeField()
#     # update_time = serializers.DateTimeField()
#     # author = serializers.StringRelatedField(label='作者')
#     author = UserSerializer(read_only=True)
#     url = serializers.HyperlinkedIdentityField(view_name="detail")
#
#     class Meta:
#         model = Article
#         fields = ['url', 'author', 'title', 'content', 'create_time', 'update_time']
#         # read_only_fields = ['author']

class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)

    class Meta:
        model = Article
        fields = '__all__'
