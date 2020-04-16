import time

from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse

# @cache_page(10)#缓存装饰器 10秒
def test_cache(request):
    # time.sleep(3)
    t1=time.time()
    # return HttpResponse(f't1 is {t1}')

    return render(request,'test_cache.html',locals())


def test_mw(request):
    print('----mw view do')
    return HttpResponse('---test middleware---')

def test_csrf(request):
    if request.method=='GET':
        return render(request,'test_csrf.html')
    elif request.method=='POST':
        return HttpResponse('--post is ok--')