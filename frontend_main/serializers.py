from .models import Post, Category
# from django.contrib.auth.models import User
from rest_framework import serializers


# class UserSerializer(serializers.ModelSerializer):
#     posts = serializers.PrimaryKeyRelatedField(many=True, queryset=Post.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'posts')


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Post
        fields = ('owner', 'title', 'categories', 'text', 'created_date', 'modified_date')

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.text = validated_data.get('text', instance.text)
        # instance.created_date = validated_data.get('created_date', instance.created_date)
        instance.modified_date = validated_data.get('modified_date', instance.modified_date)


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('title', 'description', )

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
