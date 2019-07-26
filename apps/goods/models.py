import datetime
from django.db import models

# Create your models here.


from django.db import models
from ckeditor.fields import RichTextField

class GoodsCategory(models.Model):
    """
    商品分类
    """
    CATEGORY_TYPE =(
        (1, "一级类目"),
        (2, "二级类目"),
        (3, "三级类目"),
    )

    name = models.CharField("类别名", default="", max_length=30, help_text="类别名")
    code = models.CharField("类别code", default="", max_length=30, help_text="类别code")
    desc = models.TextField("类别描述", default="", help_text="类别描述")

    category_type = models.IntegerField("分类级别", choices=CATEGORY_TYPE)
    parent_category = models.ForeignKey("self", on_delete=models.CASCADE,
                                        null=True, verbose_name="父目录", related_name="sub_cat")
    is_tab = models.BooleanField("是否导航栏", default=False)
    add_time = models.DateTimeField("添加时间", auto_now_add=True)

    class Meta:
        verbose_name = "商品分类"
        verbose_name_plural = verbose_name

    def get_sub_cat(self):
        return self.sub_cat.all()


class GoodsCategoryBrand(models.Model):
    """
    某一大类下的宣传商标
    """
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品分类")
    name = models.CharField("品牌名", default="", max_length=30)
    desc = models.CharField("品牌描述", default="", max_length=150)
    image = models.ImageField(upload_to="brands/")
    add_time = models.DateTimeField("添加时间", auto_now_add=True)

class Goods(models.Model):
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, verbose_name="商品分类")
    goods_sn = models.CharField("商品唯一编号", max_length=50, unique=True)
    name = models.CharField("商品名称", max_length=30)
    click_num = models.IntegerField("点击数", default=0)
    sold_num = models.IntegerField("售卖数量", default=0)
    fav_num = models.IntegerField("收藏数", default=0)
    goods_num = models.IntegerField("商品数量", default=0)
    market_price = models.IntegerField("市场价", default=0)
    shop_price = models.IntegerField("售价", default=0)
    goods_brief = models.TextField("商品简短描述", max_length=500)
    goods_desc = RichTextField("商品描述")
    ship_free = models.BooleanField("是否承担运费", default=True)
    goods_front_image = models.ImageField("封面图", upload_to="goods/images/", null=True,
                                          blank=True)
    is_new = models.BooleanField("是否新品", default=False)
    is_hot = models.BooleanField("是否热销", default=False)
    add_time = models.DateTimeField("添加时间", auto_now_add=True)


    class Meta:
        verbose_name = "商品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class GoodsImage(models.Model):
    """商品轮播图"""
    # goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品",related_name="goods")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, verbose_name="商品")
    image = models.ImageField("商品图片", upload_to="goods/images/")
    add_time = models.DateTimeField("添加时间", auto_now_add=True)


class Banner(models.Model):
    """
    首页轮播图
    """
    # goods = models.ForeignKey(Goods,on_delete=models.CASCADE, verbose_name="商品", related_name="goods")
    goods = models.ForeignKey(Goods,on_delete=models.CASCADE, verbose_name="商品")
    image = models.ImageField("轮播图片", upload_to="banner/")
    index = models.IntegerField("论播顺序", default=0)
    add_time = models.DateTimeField("添加时间", auto_now_add=True)

class IndexAd(models.Model):
    category = models.ForeignKey(GoodsCategory, on_delete=models.CASCADE, related_name="category")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE, related_name="goods")

class HotSearchWords(models.Model):
    keywords = models.CharField("热搜词", max_length=50, default="")
    index = models.IntegerField("排序", default=0)
    add_time = models.DateTimeField("添加时间", auto_now_add=True)


