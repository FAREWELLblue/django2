from django.contrib import admin
from .models import Book,Author

# Register your models here.

class BookManager(admin.ModelAdmin):
    list_display = ['id','title','pub','price','market_price']# 列表显示
    list_display_links = ['title']# 点击跳转的位置
    list_filter = ['pub']# 右侧过滤器
    search_fields = ['title','id']#搜索框,参数是搜索的列
    list_editable = ['price','market_price'] #在页面可以直接修改不用进详情页
class AuthorManager(admin.ModelAdmin):
    list_display = ['id','name','age']
    list_display_links = ['name']  # 点击跳转的位置

admin.site.register(Book,BookManager)
admin.site.register(Author,AuthorManager)
