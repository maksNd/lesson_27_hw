from rest_framework import serializers

from ads.models import Ad, Category
from users.serializers import UserSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    # category = serializers.SlugRelatedField(slug_field='name', read_only=True)
    category = CategorySerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
