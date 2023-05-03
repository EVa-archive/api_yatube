from posts.models import Group, Post, Comment
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    group = serializers.SlugRelatedField(slug_field='slug',
                                         read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'text', 'author', 'image',
                  'pub_date', 'group')


class GroupSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description', 'author')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username',
                                          read_only=True)
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
