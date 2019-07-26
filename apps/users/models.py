import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ("male", "男"),
        ("female", "女")
    )

    name = models.CharField("姓名", max_length=30, blank=False, null=False)
    birthday = models.DateField("生日", null=True, blank=True)
    gender = models.CharField("性别", max_length=6, choices=GENDER_CHOICES,
                              default="female")
    mobile = models.CharField("电话", max_length=11, blank=False, unique=True)
    email = models.EmailField("email")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

class VerifyCode(models.Model):
    code = models.CharField("验证码", max_length=10)
    mobile = models.CharField("手机号", max_length=11)
    add_time = models.DateTimeField("添加时间", auto_now=True)

    class Meta:
        verbose_name = "验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code

