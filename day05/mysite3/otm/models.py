from django.db import models

# Create your models here.
class Publisher(models.Model):
    #一
    name = models.CharField(max_length=20,verbose_name='名字')
class Book(models.Model):
    #多
    title = models.CharField(max_length=11,verbose_name='书名')
    publisher = models.ForeignKey(Publisher)
'''
    一对多创建外键:
        方案1:
        p1=Publisher.objects.create(name='清华大学出版社')
        b1=Book.objects.create(name='Python',publisher=a1)
        方案2:(最优解)
        p1=Publisher.objects.create(name='清华大学出版社')
        b1=Book.objects.create(name='Python',publisher_id=1)
        正向查询:book--Publisher
            book.publisher可获得对应的Publisher对象
        反向查询:隐藏属性book_set 等价于管理器对象objects
            pub1=Publisher.objects.get(name='清华大学出版社')
            books = pub1.book_set.all() 通过book_set获取pub1对应的多个book对象
        删除:
            on_delete:默认CASCADE,可以删,两表都删
            
            
'''