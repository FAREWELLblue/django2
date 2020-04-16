#模拟消费者
import redis
import json

r = redis.Redis(host='127.0.0.1',port=6379,db=0,password='123456')
while True:
    task = r.brpop('pypc',5)
    print(task)
    if task:
        json_obj=json.loads(task[1].decode())
        print(json_obj)