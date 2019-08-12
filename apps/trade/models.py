from datetime import datetime

from django.db import models

from goods.models import Goods
from users.models import UserProfile
# Create your models here.

from django.contrib.auth import get_user_model

User = get_user_model()

class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
            verbose_name="用户")
    goods = models.ForeignKey(Goods, on_delete=models.CASCADE,
            verbose_name="商品")
    nums = models.IntegerField("购买数量", default=0)
