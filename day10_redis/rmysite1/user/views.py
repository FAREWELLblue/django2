from django.http import HttpResponse
from django.shortcuts import render
import redis

from user.models import User

r=redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

# Create your views here.
def user_detail(request,user_id):
    #/user/detail/1
    cache_key='user:%s'%(user_id)
    #先查缓存
    if r.exists(cache_key):
        data=r.hgetall(cache_key)
        #{'nickname':'blue'}
        new_data={k.decode():v.decode() for k,v  in data.items()}
        nickname=new_data['nickname']
        age=new_data['age']
        html=f'nickname is {nickname},age is{age}'
        return HttpResponse(html)
    #无缓存数据
    users=User.objects.filter(id=user_id)
    user=users[0]
    nickname=user.nickname
    age=user.age
    html=f'mysql nickname is {nickname},age if {age}'
    #更新缓存
    r.hmset(cache_key,{'nickname':nickname,'age':age})
    r.expire(cache_key,15)

    return HttpResponse(html)

def user_update(request):
    #更新用户个人信息
    #/user/update?user_id=xx&&nickname=xxx&age=xxx
    user_id=request.GET.get('user_id')
    nickname=request.GET.get('nickname')
    age=request.GET.get('age')

    try:
        user=User.objects.get(id=user_id)
    except Exception as e:
        return HttpResponse('--no --user--')
    #先更新数据库
    if nickname:
        user.nickname=nickname
    if age:
        user.age=age
    user.save()
    #后删除缓存
    cache_key='user:%s'%(user_id)
    r.delete(cache_key)
    return HttpResponse('%s update is ok'%(user_id))