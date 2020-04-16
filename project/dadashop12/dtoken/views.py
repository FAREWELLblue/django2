import hashlib
import json
import time
import jwt
from django.conf import settings

from user.models import UserProfile
from django.http import JsonResponse
from django.shortcuts import render


# 10200-10299状态码
# Create your views here.

def make_token(username, exp=3600 * 24):
    now = time.time()
    payload = {'username': username, 'exp': now + exp}
    return jwt.encode(payload, settings.JWT_TOKEN_KEY)


def tokens(request):
    if request.method != 'POST':
        result = {'code': 10200, 'error': 'Please use POST'}
        return JsonResponse(result)
    json_str = request.body
    json_obj = json.loads(json_str)
    username = json_obj['username']
    password = json_obj['password']
    # TODO 校验参数

    old_users = UserProfile.objects.filter(username=username)
    if not old_users:
        result = {'code': 10201, 'error': 'The username or password is wrong!'}
        return JsonResponse(result)
    user = old_users[0]
    m = hashlib.md5()
    m.update(password.encode())
    if m.hexdigest() != user.password:
        result = {'code': 10202, 'error': 'The username or password is wrong!'}
        return JsonResponse(result)

    # 签发token
    token = make_token(username)

    result = {'code': 200, 'username': username, 'data': {'token': token.decode()}, 'carts_count': 0}
    return JsonResponse(result)
