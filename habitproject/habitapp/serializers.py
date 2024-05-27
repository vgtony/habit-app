from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import TextData


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


class TextDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextData
        fields = ['url', 'text', 'created_at', 'updated_at']
