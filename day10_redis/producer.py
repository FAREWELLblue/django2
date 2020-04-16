'''
    模拟生产者
'''
import json
import redis
r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')

json_obj={'task':'send_email','from':'blue','to':'12345@qq.com','content':'这是内容'}
json_str=json.dumps(json_obj)
#先进先出 lpush rpop
r.lpush('pypc',json_str)