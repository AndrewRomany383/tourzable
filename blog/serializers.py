from rest_framework import serializers
from parler_rest.serializers import TranslatableModelSerializer, TranslatedFieldsField
from taggit.serializers import TaggitSerializer, TagListSerializerField
from .models import Post, Category

class CategorySerializer(TranslatableModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']


class CategorySerializerMultiLanguage(TranslatableModelSerializer):
    translations = TranslatedFieldsField(shared_model=Category)
    class Meta:
        model = Category
        fields = ['id', 'title', 'translations']


class PostSerializer(TaggitSerializer, TranslatableModelSerializer):
    tags = TagListSerializerField()
    category = CategorySerializer()
    class Meta:
        model = Post
        fields = ['id', 'title', 'tags', 'created_at', 'description', 'slug', 'image', 'category']



class PostSerializerMultiLanguage(TaggitSerializer, TranslatableModelSerializer):
    tags = TagListSerializerField()
    category = CategorySerializerMultiLanguage()
    class Meta:
        model = Post
        fields = ['id', 'title', 'tags', 'created_at', 'description', 'slug', 'image', 'category']






















