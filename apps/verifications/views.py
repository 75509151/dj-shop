from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from django_redis import get_redis_connection
from utils import constants

# Create your views here.

class ImagesCodeView(APIView):

    def get(self, request, image_code_id):
        # TODO:
        # text, image = captcha.generate_captcha()
        text, image = "验证码", ""
        redis_conn = get_redis_connection("verify_codes")
        redis_conn.setex("img_%s" % image_code_id, constants.IMAGE_CODE_REDIS_EXPIRES, text)
        return HttpResponse(image, context_type="image/jpg")

