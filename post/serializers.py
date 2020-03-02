from rest_framework import serializers

from core.models import Post


class PostListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'author_name', 'likes')
        fields_read_only = ('id',)


class PostDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'likes')
        fields_read_only = ('id',)


class PostLikeUnLikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'likes',)
        fields_read_only = ('id',)
