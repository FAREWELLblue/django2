from django.db import models

# Create your models here.
class Book(models.Model):
    id=models.IntegerField('id',db_index=1,primary_key=True)
    title = models.CharField("书名",max_length=50,default='',primary_key=True )# 最大长度50
    price = models.DecimalField("图书定价",max_digits=7,decimal_places=2 ,default=0.0)# 最大位数,其中保留两位
    desc=models.CharField('描述',max_length=100,default='')
    #新添字段时,记住加default值
    pub = models.CharField('出版社',max_length=200,default='')
    market_price = models.DecimalField('推书零售价',max_digits=7,decimal_places=2,default=0.0)
    is_active = models.BooleanField('是否活跃',default=True)
    class Meta:
        db_table='book'# 参数 数据表名 mysql中数据表的名称
        verbose_name='图书'# 参数 单数 例如图书列表页的添加
        verbose_name_plural=verbose_name# 参数 复数名 复数形态,admin后台首页,

    def __str__(self):
        return f"书名{self.title},出版社{self.pub},价格{self.price}"
class Author(models.Model):
    name = models.CharField('姓名',max_length=11,default='')
    age = models.IntegerField('年龄',default=1)
    email = models.EmailField('邮箱',null=True)
    class Meta:
        db_table='author'
        verbose_name='作者'
        verbose_name_plural=verbose_name
