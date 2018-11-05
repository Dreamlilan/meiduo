from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django_redis import get_redis_connection
from rest_framework.views import APIView

# 生成图片验证码
from libs.captcha.captcha import captcha
from verifications import constant


class RegisterImageCodeView(APIView):

    """
    生成图片验证码
    GET： verifications/imagecodes/(?P<image_code_id>.+)/
    需要通过JS生成一个唯一码(UUID),以确保后台对图片进行校验
    """
    def get(self,request,image_code_id):
        """
        通过第三方库,生成图片和验证码,我们需要对验证码进行redis保存

        思路：
        1.创建图片和验证码
        2.通过redis进行保存验证码,需要在设置中添加 验证码数据库选项
        3.将图片返回

        """
        # 1 通过图片和验证码
        text,image = captcha.generate_captcha()
        # 2 通过redis进行保存验证码
        # 连接redis
        redis_conn = get_redis_connection('code')
        # 保存图片验证码  img_%s ： 在image_code_id前面加了一个前缀
        redis_conn.setex('img_%s' % image_code_id, constant.IMAGE_CODE_EXPIRE_TIME, text)

        # 3. 返回响应
        return HttpResponse(image, content_type='image/jpeg')

















