from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField("用户名", max_length=30, unique=True)#unique唯一索引
    password = models.CharField("密码", max_length=32)
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    #时间字段 -数据库里存储的UTC时间,模板层会根据settings.py中的Timezone配置修正显示时间
    def __str__(self):
        return "用户" + self.username