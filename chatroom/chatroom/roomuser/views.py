from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
from room.models import Room_list
from roomuser.models import RoomUser
from userapp.models import User


def setView(request):
    rid = request.session.get('rid')
    uid = request.session.get('uid')
    try:
        user=RoomUser.objects.get(room_id=rid,user_id=uid)
        if not user.is_active:
            return JsonResponse({'code':404,'data':'sent out'})

    except:
        RoomUser.objects.create(room_id=rid,user_id=uid)
    print('创建成功')
    return JsonResponse({'code': 200, 'data': 'set success'})


def getView(request):
    rid = request.session.get('rid')
    # uid = request.session.get('uid')
    data=RoomUser.objects.filter(room_id=rid,is_active=1)
    # print('************************',data)
    list=[users.user.username for users in data]


    return JsonResponse({'code': 200, 'data': list})


def outView(request):
    # print('000000000000000000000',request.GET.get('name'))
    outname=request.GET.get('name')
    outrid=request.session.get('rid')
    outuid=User.objects.get(username=outname).id
    print(f'outuid is {outuid},outrid is {outrid}')
    item = RoomUser.objects.get(user_id=outuid,room_id=outrid)
    item.is_active=0
    item.save()
    return JsonResponse({'code':200,'data':'out success'})