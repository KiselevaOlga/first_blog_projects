from rest_framework import serializers
from .models import Post, PostNumber, PostTopic, PostCommentator


class PostNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostNumber
        fields = ['id', 'isbn_10', 'isbn_13']


class PostTopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostTopic
        fields = ['id', 'topic']


class PostCommentatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostCommentator
        fields = ['id', 'name', 'surname', 'text']


class PostSerializer(serializers.ModelSerializer):
    number = PostNumberSerializer(many=False)
    topics = PostTopicSerializer(many=True)
    commentators = PostCommentatorSerializer(many=True)

    class Meta:
        model = Post
        fields = ['id', 'title', 'author', 'published_date', 'number', 'topics', 'commentators']

