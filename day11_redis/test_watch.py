'''
    测试流水线
'''
import time

import redis
pool=redis.ConnectionPool(host='127.0.0.1',db=0,port=6379,password='123456')
r=redis.Redis(connection_pool=pool)

def double_account(user_id):
    key='account_%s'%(user_id)
    with r.pipeline() as pipe:
        while True:
            try:
                # watch key
                pipe.watch(key)# 直接发给redis
                value=int(r.get(key))
                value *=2
                print('value is %s'%(value))
                print('sleep start')
                time.sleep(10)
                print('sleep end')
                pipe.multi()
                pipe.set(key,value)
                #由于我们使用了 watch 所以execute可能胡出现异常[watch key]在watch之后,被其他客户端修改了
                pipe.execute()
                break
            except redis.WatchError:
                print('--key changed')
                continue
    return int(r.get(key))
if __name__ == '__main__':

