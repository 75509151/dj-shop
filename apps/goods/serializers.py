from rest_framework import serializers
from .models import GoodsCategory

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
