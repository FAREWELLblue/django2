from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('作家姓名',max_length=11)#,verbose_name='作家名称')

class Wife(models.Model):
    name=models.CharField(max_length=11)#,verbose_name='妻子名称')
    author = models.OneToOneField(Author)

'''
    一对一创建外键
        方案1:
            a1=Author.objects.create(name='王老师')
            w1=Wife.objects.create(name='王夫人',author=a1)
        方案2:(最优解)
            a2=Author.objects.create(name='郭老师')
            w2=Wife.objects.create(name='郭夫人',author_id=a2.id)
        正向查询:wife--author,外键在哪个表上,那个表查另一个表为正向查询
            wife2 = Wife.objects.get(name='王夫人')
            print(wife2.name,'的老公是',wife2.author.name)
        反向:使用的隐藏属性.外键创建时Django会在原表生成隐藏属性
            author1 =  Author.objects.get(name='王老师')
            print(author1.name,'的妻子是',author1.wife.name)
        级联删除:
            默认on_delete cascade,两个都删 1.11*版本
        作用:
        1.第三方授权
        2.冷热数据分离
        3.开发过程->新手问题
'''
