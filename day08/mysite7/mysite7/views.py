import csv
import os
import time

from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from django.http import HttpResponse
from django.conf import settings

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

def test_page(request):
    all_data=['a','b','c','d','e']
    paginator=Paginator(all_data,2)
    cur_page=request.GET.get('page',1)
    page=paginator.page(cur_page)
    return render(request,'test_page.html',locals())

def upload_view(request):
    if request.method == 'GET':
        return render(request, 'test_upload.html')
    elif request.method == "POST":
        file_obj=request.FILES['myfile']
        fpath=os.path.join(settings.MEDIA_ROOT,file_obj.name)
        print('地址',fpath)
        with open(fpath,'wb') as f:
            data=file_obj.file.read()
            f.write(data)
        return HttpResponse(f'--{file_obj.name}upload is ok')
def test_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="mybook.csv"'
    all_data=[{'id':1,'title':'Python1'},
              {'id':2,'title':'Python2'},
              {'id':3,'title':'Python3'},
              {'id':4,'title':'Python4'},]
    writer=csv.writer(response)
    for data in all_data:
        writer.writerow([data['id'],data['title']])
    return response