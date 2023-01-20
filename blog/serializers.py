from rest_framework import serializers
from .models import Post, Category
from rest_framework.renderers import JSONRenderer
import io
from rest_framework.parsers import JSONParser


class PostSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Post
        fields = "__all__"


class CatSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Category
        fields = "__all__"

# class PostModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# class PostSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=150)
#     content = serializers.CharField()
#     time_create = serializers.DateTimeField(read_only=True)
#     time_update = serializers.DateTimeField(read_only=True)
#     is_published = serializers.BooleanField(default=True)
#     cat_id = serializers.IntegerField()
#
#     def create(self, validated_data):
#         return Post.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.content = validated_data.get("content", instance.content)
#         instance.time_update = validated_data.get("time_update", instance.time_update)
#         instance.is_published = validated_data.get("is_published", instance.is_published)
#         instance.cat_id = validated_data.get("cat_id", instance.cat_id)
#         instance.save()
#         return instance

# def enCode():
#     model = PostModel('title 1', 'post 1')
#     modelsSr = PostSerializer(model)
#     print(modelsSr.data)
#     json = JSONRenderer().render(modelsSr.data)
#     print(json)
#
#
# def deCode():
#     stream = io.BytesIO(b'{"title":"title 1","content":"post 1"}')
#     print(stream)
#     data = JSONParser().parse(stream)
#     print(data)
#     serializer = PostSerializer(data=data)
#     print(serializer)
#     serializer.is_valid()
#     print(serializer.validated_data)
