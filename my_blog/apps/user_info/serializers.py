from rest_framework import serializers
from apps.user_info.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'last_login', 'date_joined']
