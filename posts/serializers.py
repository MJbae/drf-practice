from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'body', 'created_at',)

    def validate(self, data):
        first_author = self.context.get("first_author")

        if data['author'] != first_author:
            raise serializers.ValidationError("not that author")

        return data


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('id', 'username',)
