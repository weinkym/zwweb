from django.db import models

class User(models.Model):
    openid=models.CharField(primary_key=True,max_length=64)
    unionid=models.CharField(max_length=64)

    nickname=models.CharField(max_length=64,null=True)
    language=models.CharField(max_length=64,null=True)
    city=models.CharField(max_length=64,null=True)
    remark=models.CharField(max_length=64,null=True)
    headimgurl=models.CharField(max_length=256,null=True)

    sex=models.IntegerField(default=0,null=True)
    subscribe_time=models.DateTimeField(verbose_name='关注时间')

    
# Create your models here.
