from django.db import models

# Create your models here.

from django.db import models
from django.contrib.auth.models import AbstractUser

"""
django认证系统自动提供用户模型类及方法，但是有些字段不能满足我们的需求。
我们就需要在继承框架给定的模型父类的基础上，再给模型添加额外的字段。
我们自定义的用户模型类创建好以后，还不能直接被Django的认证系统所识别，
需要在配置文件中告知Django认证系统优先使用我们自定义的模型类。
"""


# Create your models here.
class User(AbstractUser):
    """用户模型类"""
    mobile = models.CharField(max_length=11, unique=True, verbose_name='手机号')

    class Meta:
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
