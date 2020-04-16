import time
import redis

pool = redis.ConnectionPool(host = '127.0.0.1',db=0,port=6379,password='123456')
r = redis.Redis(connection_pool=pool)

def withpipeline(r):
    p = r.pipeline()
    for i in range(1000):
        key = 'test1' + str(i)
        value = i+1
        p.set(key, value)
    p.execute()

def withoutpipeline(r):
    for i in range(1000):
        key = 'test2' + str(i)
        value = i+1
        r.set(key, value)
if __name__ == '__main__':
    t1=time.time()
    # withpipeline(r)
    withoutpipeline(r)
    t2=time.time()
    #with ' 0.10380077362060547'
    #without'0.3118870258331299'
    print(f'time is {t2-t1}')
