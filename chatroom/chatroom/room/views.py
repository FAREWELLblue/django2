import json
import shutil
import simplejson
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import *
from userapp.models import User
from django.conf import settings
import os
# Create your views here.
def check_login(request):
    if request.session.get('username'):
        return True
    else:
        return False

def index(request):
    return render(request, 'index.html')
def room(request):
    if request.method == "GET":
        print(request.session.get('username'))
        # 判断是否已登录
        if check_login(request):
            #获取聊天室列表
            room_list=Room_list.objects.values('id','roomname','user__username','introduce')
            #queryset转json
            room_list=json.dumps(list(map(dict,room_list)))
            print(room_list)
            if room_list:
                return HttpResponse(json.dumps({'code': '20', "data": room_list,'user':request.session.get('username')}))
            else:
                return HttpResponse(json.dumps({'code': '41', 'data': '暂时没有聊天室'}))
        else:
            return HttpResponse(json.dumps({'code': '40', 'data': {"msg": "没有登录"}, }))

    elif request.method == "POST":
        #新建聊天室
        #获取数据
        request_json=simplejson.loads(request.body.decode())
        r_name = request_json.get("r_name")
        r_intro = request_json.get('r_intro')
        username = request.session.get('username')
        # print(owner,'创建',r_name,'简介',r_intro)
        # 检查数据
        if Room_list.objects.filter(roomname=r_name):
            return HttpResponse(json.dumps({'code': '43', 'msg': '聊天室名称重复'}))
        # 录入数据库
        owner = User.objects.get(username=username)
        try:
            Room_list.objects.create(roomname=r_name,introduce=r_intro,user=owner)
        except Exception as e:
            print('新聊天室入库错误',e)
            return HttpResponse(json.dumps({'code':'42','msg':'聊天室入库错误'}))
        return HttpResponse(json.dumps({"code": '21', 'msg': '创建成功'}))


def chat(request):
    if not check_login(request):
        return HttpResponseRedirect('/user/login')

    if request.method=='GET':
        print(request.GET)
        roomname=request.GET.get('rname')
        # 获取rid
        r=Room_list.objects.filter(roomname=roomname)
        if r:
            rid=r[0].id
            oname=r[0].user.username
        else:
            #没有找到这个聊天室
            return HttpResponse('没有找到聊天室,不要自己拼连接哟')
        request.session['roomname']=roomname
        request.session['rid']=rid
        request.session['ownername']=oname
        return render(request,'room.html',{'roomname':roomname,'username':request.session.get('username')})
    elif request.method=='POST':
        #判断请求
        request_json = simplejson.loads(request.body.decode())
        if request_json.get('msg') == 'say':
            #获取数据
            mes = request_json.get('message')
            uid=request.session.get('uid')
            rid=request.session.get('rid')
            print(uid,rid,mes)
            try:
                # 将聊天记录写入数据库
                Record.objects.create(user_id=uid,room_id=rid,content=mes)
            except Exception as e:
                print('发送消息出错',e)
                return json.dumps({'code': '40', 'msg': "发送失败"})
            return HttpResponse(json.dumps({'code': '11', 'msg': "发送成功"}))
        elif request_json.get('msg') == 'read':
            r_name=request.session['roomname']
            oname=request.session['ownername']
            print('room-name----------', r_name)
            records=Record.objects.filter(room__roomname=r_name).values('user__username','content','sent_time')
            print(records)
            if records:
                records = list(map(dict, records))
                for record in records:
                    record['sent_time'] = record['sent_time'].strftime('%Y-%m-%d %H:%M:%S')
                print(records)
                return HttpResponse(json.dumps({'code': '20', 'data': records,'user':request.session['username'],'owner':oname}))
            else:
                return HttpResponse(json.dumps({'code': '40', 'msg': '无聊天记录','user':request.session['username'],'owner':oname}))
        else:
            return HttpResponse(json.dumps({'code': '41', 'msg': '无法识别ajax代码'}))

def upload(request):
    if request.method=='POST':
        fl=request.FILES['myfile']
        rid=request.session['rid']
        print('上传的文件名',fl.name)
        fname=fl.name
        if Files.objects.filter(fname=fl.name,room_id=rid):
            #文件有重名
            print('有重名',type(fname))
            point = fname.find('.')
            fname=fname[:point]+'(2)'+fname[point:]
            print('重名文件名',fname)
        os.mkdir(os.path.join(settings.MEDIA_ROOT,f'{rid}/'))
        filename=os.path.join(settings.MEDIA_ROOT,f'{rid}/'+fname)
        with open(filename,'wb') as f:
            f.write(fl.file.read())
        Files.objects.create(fname=fname,fpath=filename,user_id=request.session.get('uid'),room_id=request.session.get('rid'))
        
        return HttpResponse('balabala')
def files(request):
    rid=request.session.get('rid')
    file_list=Files.objects.filter(room_id=rid).values('fname','updated_time')
    file_list=list(map(dict,file_list))
    for file in file_list:
        file['updated_time']=file['updated_time'].strftime('%Y-%m-%d %H:%M:%S')
    return  HttpResponse(json.dumps(file_list))

def leave(request):
    rid=request.session['rid']
    if request.session['ownername']==request.session['username']:
        try:
            room=Room_list.objects.get(id=rid)
            room.delete()
            print(os.path.join(settings.MEDIA_ROOT,f'{rid}/'))
            shutil.rmtree(os.path.join(settings.MEDIA_ROOT,f'{rid}/'))
        except Exception as e:
            print('解散聊天室时出错',e)
            return HttpResponse(json.dumps({'code':'40','msg':'解散失败'}))
    del request.session['roomname']
    del request.session['rid']
    return HttpResponse(json.dumps({'code':'21','msg':'退出成功'}))