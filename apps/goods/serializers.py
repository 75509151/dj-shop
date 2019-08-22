from rest_framework import serializers
from .models import GoodsCategory, Banner, Goods

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

class IndexGoodsSerializer(serializers.ModelSerializer):
    banners = BannerSerializer(many=True)
    goods = serializers.SerializerMethodField()
    sub_cat = Category2Serializer(many=True)
    ad_goods = serializers.SerializerMethodField()


    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id)|Q(category__parent_id=obj.id)|Q(
            category__parent_category__parent_category_id=obj.id))

        return GoodsSerializer(all_goods, many=True, context={"request":self.context["request"]})


    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"

