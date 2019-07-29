from django.db import models
import time

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


VALIDITYE_TYPE_DEFAULT=0
VALIDITYE_TYPE_TIME=1
VALIDITYE_TYPE_COUNT=2
VALIDITYE_TYPE_VIP=9999

TIME_FORMAT="%Y-%m-%d %H:%M:%S"

class Account(models.Model):
    openid=models.CharField(primary_key=True,max_length=64)
    validity_time=models.DateTimeField(default='1970-01-01 08:00:00')
    validity_type=models.IntegerField(default=0,null=True)
    lastupdate_time=models.DateTimeField(default='1970-01-01 08:00:00')
    lastuse_time=models.DateTimeField(default='1970-01-01 08:00:00')
    validity_count=models.IntegerField(default=0,null=True)

    def isCount(self):
        if self.validity_type == VALIDITYE_TYPE_DEFAULT or self.validity_type == VALIDITYE_TYPE_DEFAULT:
            return True
        return False

    def isValid(self):
        if type(self.openid) is not str:
            return False
        if len(self.openid) <= 0:
            return False

        if self.isCount() is True:
            return self.validity_count > 0
        
        vt = time.strptime(self.validity_time,fmt='TIME_FORMAT')
        return vt > time.localtime()


    def updateOne(self):
        self.lastuse_time=time.strftime(TIME_FORMAT, time.localtime())
        if self.isCount() is True:
            self.validity_count = self.validity_count - 1
        self.save()


    @classmethod
    def create(cls, openid):
        obj = cls(openid=openid)
        obj.validity_time=time.strftime(TIME_FORMAT, time.localtime(0))
        obj.lastupdate_time=time.strftime(TIME_FORMAT, time.localtime())
        obj.validity_type=VALIDITYE_TYPE_DEFAULT
        obj.validity_count=10
        return obj




    

    
# Create your models here.
