from django.shortcuts import render
from .models import GoodsCategory, Banner, Goods
from rest_framework import viewsets, mixins
from .serializers import CategorySerializer, BannerSerializer, IndexCategorySerializer, GoodsSerializer

# Create your views here.


class CategoryView(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):

    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer
    paginator = None



class BannerView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer
    paginator = None

class IndexCategoryView(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = GoodsCategory.objects.filter(is_tab=True,name__in=["生鲜食品", "酒水饮料"])
    serializer_class = IndexCategorySerializer
    paginator = None

class GoodsView(mixins.ListModelMixin, mixins.RetrieveModelMixin,
                mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                mixins.CreateModelMixin,viewsets.GenericViewSet):

    serializer_class = GoodsSerializer
    queryset = Goods.objects.all()
