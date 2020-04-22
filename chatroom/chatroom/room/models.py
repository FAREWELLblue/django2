from django.db import models
from userapp.models import User

# Create your models here.
class Room_list(models.Model):
    roomname=models.CharField('聊天室名称',max_length=50,unique=True)
    introduce=models.TextField('聊天室简介',default='无')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    updated_time = models.DateTimeField('更新时间', auto_now=True)
    is_active=models.BooleanField('活跃',default=True)
    owner=models.IntegerField('管理员',default=0)
    # user=models.ManyToManyField(User)# 用户列表
    def __str__(self):
        return f'聊天室名称:{self.roomname},聊天室管理员:{self.owner},聊天室简介:{self.introduce}'
    class Meta:
        verbose_name='聊天室'
        verbose_name_plural='聊天室列表'
        db_table='rooms'

class Record(models.Model):
    content = models.TextField('消息内容')
    sent_time=models.DateTimeField('发送时间', auto_now=True)
    is_active = models.BooleanField('活跃', default=True)
    user=models.ForeignKey(User)
    room=models.ForeignKey(Room_list)
    def __str__(self):
        return f'{self.user}:{self.content},时间是{self.sent_time}'
    class Meta:
        db_table='record'
        # verbose_name='聊天记录'
        # verbose_name_plural=verbose_name

class Files(models.Model):
    fname=models.CharField('文件名',max_length=50)
    fpath=models.CharField('文件位置',max_length=70)
    updated_time=models.DateField('上传时间',auto_now=True)
    user=models.ForeignKey(User)
    room=models.ForeignKey(Room_list)
    def __str__(self):
        return f'{self.user}在{self.room}上传{self.fname},存放在{self.fpath}'
    class Meta:
        db_table='files'
        verbose_name='文件'
        verbose_name_plural='文件列表'

    
