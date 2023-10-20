from rest_framework import serializers
from apps.article.models import Article, Category
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


class CategorySerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='category-detail')

    class Meta:
        model = Category
        fields = '__all__'
        read_only_fields = ['create_time']  # 创建日期不需要修改


class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer(read_only=True)
    category = CategorySerializer(read_only=True)
    category_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)

    # category_id字段验证
    def validate_category_id(self, value):
        if not Category.objects.filter(id=value).exists() and value is not None:
            raise serializers.ValidationError("Category with id {} not exits.".format(value))
        return value

    class Meta:
        model = Article
        fields = '__all__'


class ArticleCategoryDetailSerializer(serializers.ModelSerializer):
    """给分类详情的嵌套序列化器"""
    url = serializers.HyperlinkedIdentityField(view_name='article-detail')

    class Meta:
        model = Article
        fields = [
            'url',
            'title',
        ]


class CategoryDetailSerializer(serializers.ModelSerializer):
    """分类详情"""
    articles = ArticleCategoryDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = [
            'id',
            'title',
            'create_time',
            'articles',
        ]
