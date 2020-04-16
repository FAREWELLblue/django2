from django.http import HttpResponse
from django.shortcuts import render


def test_static(request):
    return render(request,'test_static.html')

def test_cookies(request):
    resp = HttpResponse('哈哈哈哈')
    resp.set_cookie('username','blue')
    #value=request.COOKIES.get('key','缺省值')
    # resp.set_cookie('username','blue',300)
    return resp
def set_session(request):
    request.session['uname']='user'
    return HttpResponse('--set seession is ok--')

def get_session(request):
    name = request.session['uname']
    return HttpResponse(f'--get session values is {name}')
