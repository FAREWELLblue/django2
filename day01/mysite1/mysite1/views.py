from django.http import  HttpResponse,HttpResponseRedirect


def page1_view(resquest):

    html = '<h1>这是编号1的页面</h1>'
    # return HttpResponse(html)
    return HttpResponseRedirect('/page2')#临时重定向,跳转到page2
    # 302 跳转依靠响应头中的location告知浏览器此次跳转的目的地

def page2_view(request):
    return HttpResponse("<h1>这是编号2的页面</h1>")


def index_view(request):
    return HttpResponse("<h1>这是主页</h1>")


def pagen_view(request,n):
    # n -> 字符串类型
    return HttpResponse(f"<h1>这是编号{n}的页面</h1>")


def cal_view(request,num1,str,num2):
    num1=int(num1)
    num2=int(num2)
    if str=='add':
        return HttpResponse(f"<h1>结果是:{num1+num2}</h1>")


def person_view(request,name,age):
    return HttpResponse(f'姓名:{name} 年龄:{age}')


def birthday_view(request,year,month,day):
    print(request.path_info)
    print(request.get_full_path())
    print(request.method)

    #获取包含查询字符串的name和值的'字典'
    print(request.GET)
    print(request.POST)
    print(request.META)

    return HttpResponse(f"生日为:{year} 年,{month}月,{day}日")
