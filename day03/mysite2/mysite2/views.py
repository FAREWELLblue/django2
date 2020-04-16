from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render

post_form = '''
<form method='post' action="/test_post">
    姓名:<input type="text" name="username">
    <input type='submit' value='登陆'>
</form>
'''


def person_view(request, name, age):
    return HttpResponse(f'姓名:{name} 年龄:{age}')


def birthday_view(request, year, month, day):
    print(request.path_info)
    print(request.get_full_path())
    print(request.method)

    # 获取包含查询字符串的name和值的'字典'
    print(request.GET)
    print(request.POST)
    print(request.META)

    return HttpResponse(f"生日为:{year} 年,{month}月,{day}日")


def test_get(requset):
    if requset.method == 'GET':
        print(requset.GET['a'])
        print(requset.GET.get('a', 'hahaha'))
        print(requset.GET.getlist('a'))
        print(requset.GET)
        return HttpResponse('test get is ok ')
    return HttpResponse('test get is error')


def test_post(request):
    if request.method == "GET":
        html = post_form
        return HttpResponse(html)
    elif request.method == "POST":
        username = request.POST['username']
        print('---testPost---')
        print(username)
        return HttpResponse('test post is ok')
    return HttpResponse('test post is error')


# def test_html(request):
#     #1 加载html
#     t= loader.get_template('test.html')
#     # 2 执行render 转换成字符串
#     html=t.render()
#     return HttpResponse(html)

def test_html(request):
    dic = {
        'username': "balabala",
        'text': 'balabalbalabal',
        'age': 18,
        'list': ['tom', 'lily', 'jack'],
        'd': {"title": "bala"},
        'func': say_hi,
        'class_obj': Dog(),
        'script': '<script>alert(11)</script>',
        # xss(Cross Site Script)跨站脚本攻击, 用户通过网站输入框,输入一段JS代码,网站接收js代码后,执行代码中的步骤,从而造成损失
        # 防范  转义用户输入 #import html   html.escape()可以转义
    }

    return render(request, 'test.html', dic)


class Dog:
    def say(self):
        return 'hahaha'


def say_hi():
    return 'hi'


def mycal(request):
    if request.method == 'GET':
        return render(request, 'mycal.html')
    elif request.method == 'POST':
        x = request.POST['x']
        y = request.POST['y']
        op = request.POST['op']
        try:
            x = int(x)
            y = int(y)
        except Exception as e:
            error = 'input is error'
            return render(request, 'mycal.html', locals())
            # return HttpResponse('The input is error')
        if op == 'add':
            result = x + y
        elif op == 'sub':
            result = x - y
        elif op == 'mul':
            result = x * y
        elif op == 'div':
            if y == 0:
                return HttpResponse('The input is error')
            else:
                result = x / y
        else:
            return HttpResponse('The op is error')
        # dic={
        #     'x':x,
        #     'op':op,
        #     'y':y,
        #     'result':result
        # }
        return render(request, 'mycal.html', locals())


def test_base(request):
    lst=['tom','jack']
    return  render(request,'base.html',locals())

def test_music(request):
    return  render(request,'music.html')

def test_sport(request):
    return  render(request,'sport.html')


def page1_view(request):
    return render(request,'page1.html')

def page2_view(request):
    return HttpResponse("我是page2")


def pagen_view(request,n):
    from django.urls import reverse
    print('-----------reverse --------------')
    print(reverse('page2'))# 可解析出别名name=page2的URL地址
    print(reverse('pn',kwargs={'n':500}))# 可解析出别名name=pn且关键字参数n为500的uyrl地址
    return HttpResponse(f'我是page{n}')
