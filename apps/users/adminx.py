import xadmin
from .models import VerifyCode

# class UserProfileAdmin(object):
    # list_display = ["name", "mobile", "email","last_login"]


class VerifyCodeAdmin(object):
    list_display = ["code", "mobile", "add_time"]

xadmin.site.register(VerifyCode, VerifyCodeAdmin)
