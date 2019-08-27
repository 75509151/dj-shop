from rest_framework import serializers
from .models import GoodsCategory, Banner, Goods, GoodsCategoryBrand, IndexAd
from django.db.models import Q

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

class BrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategoryBrand
        fields = "__all__"

class IndexCategorySerializer(serializers.ModelSerializer):
    brands = BrandsSerializer(many=True).data
    goods = serializers.SerializerMethodField()
    sub_cat = Category2Serializer(many=True)
    ad_goods = serializers.SerializerMethodField()


    def get_goods(self, obj):
        all_goods = Goods.objects.filter(Q(category_id=obj.id)|Q(category__parent_category_id=obj.id)|Q(
            category__parent_category__parent_category_id=obj.id))

        return GoodsSerializer(all_goods, many=True, context={"request":self.context["request"]}).data

    def get_ad_goods(self, obj):
        goods_json = {}
        ad_goods = IndexAd.objects.filter(category_id=obj.id,)
        if ad_goods:
            goods_ins = ad_goods[0].goods
            goods_json = GoodsSerializer(goods_ins).data
        return goods_json
        
    class Meta:
        model = GoodsCategory
        fields = "__all__"

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Goods
        fields = "__all__"

