from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from users.models import User

# import os
# if not os.environ.get("DJANGO_SETTINGS_MODULE"):
#     os.environ.setdefault("DJANGO_SETTINGS_MODULE", "drf_demo.settings")


class RegisterUsernameCountView(APIView):
    """
    获取用户名的个数
    GET:  /users/usernames//count/(?P<username>\w{5,20})
    """
    def get(self,request,username):

        # 1.后端接收用户名,通过模型查询,获取用户名个数
        count = User.objects.filter(username=username).count()

        # 2.组织数据
        context = {
            'count':count,
            'username':username
        }

        # 3.返回响应
        return Response(context)


class RegisterPhoneCountView(APIView):
    """
    查询手机号的个数
    GET ： /users/phones/(?P<mobile>1(345789)\d{9})/count/
    """
    def get(self,request,mobile):

        # 1. 通过模型类查询获取手机号个数
        count = User.objects.filter(mobile=mobile)

        #  2. 组织数据
        context = {
            'count':count,
            'mobile':mobile
        }

        # 3. 返回响应
        return Response(context)












