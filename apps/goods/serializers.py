from rest_framework import serializers
from .models import GoodsCategory, Banner

class Category3Serializer(serializers.ModelSerializer):


    class Meta:
        model = GoodsCategory
        fields = "__all__"

class Category2Serializer(serializers.ModelSerializer):

    sub_cat = Category3Serializer(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"

class CategorySerializer(serializers.ModelSerializer):

    sub_cat = Category2Serializer(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"

class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = "__all__"
