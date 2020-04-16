from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField('作家',max_length=11)

class Book(models.Model):
    title = models.CharField('书名',max_length=11)
    #属性
    authors = models.ManyToManyField(Author)
'''
    多对多创建:
    因为ManyToMany在book表,所以要先创建Author
    author1 = Author.objexts.create(name='王老师')
        Author表有隐藏属性book_set.
    book1=author1.book_set.create('Python')#一个作者可以写多本书,写一本create一本
        1在book表中创建book11
        2在第三张表里创建book11和author1
    author2 = Author.objexts.create(name='郭老师')
        使用author为book1添加一个作者
    author2.book_set.add(book1)#一本书可以有多个作者,多一个作者,add一次
        book对象也可以绑定新作者
    b2=Book.objecte.create(title='django')
    b2.authors.create(name='吕老师')
    
    正向查询:book-->author
        book.authors.all()-->获取book对应的所有的authors信息
        book.authors.filter()-->筛选获取book对应的作者
    反向查询: author-->book,调用隐藏属性
        author.book_set.all()/filter()
        author.book_set.clear()可以删除author绑定的所有书
        
'''