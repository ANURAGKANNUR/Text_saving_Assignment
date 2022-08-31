from rest_framework import serializers
from .models import Snippet,Tag


class SnippetSerializer(serializers.ModelSerializer):
    createdby=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Snippet
        fields='__all__'

class SnippetUpdateSerializer(serializers.ModelSerializer):
    createdby=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Snippet
        fields=[
            'title','content','tag','createdby'
        ]
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model=Tag
        fields='__all__'

class SnippetSerializerUrl(serializers.HyperlinkedModelSerializer):
    # createdby=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Snippet
        fields=['url','title']

class TagSerializerURL(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Tag
        fields=['url']