import redis
r = redis.Redis(host='127.0.0.1',port=6379,password='123456',db=0)

#通用命令演示

# key_list=r.keys('*')
# for key in key_list:
#     print(key)

# print(r.exists('l1'))

# r.lpush('pyl1','a','b','c','d','e')
# print(r.lrange('pyl1',0,-1))
# print(r.rpop('pyl1'))
# print(r.ltrim('pyl1',1,3))

#############string################
# r.set('pyusername','blue')
# print(r.get('pyusername'))
#
# r.mset({'pyusername1':'wanglaoshi','pyusername2':'lvlaoshi'})
# print(r.mget('pyusername1', 'pyusername2'))

# r.incr('pyage')
# 返回值是int
# print(r.incr('pyage',10))
# key='%s:login'%(user_id)
# r.setbit(key,0,1)
# r.setbit(key,4,1)
# r.bitcount(key)

# r.hset('pyh1','name','blue')
# print(r.hget('pyh1','name'))
# print(r.hgetall('pyh1'))

#############set######################
# 返回值集合
# r.sadd('pys1','a','b','c')
# print(r.smembers('pys1'))
# 返回值 字节串
# print(r.spop('pys1'))

# r.sadd('pys2','a','b','c')
# print(r.sinter('pys1', 'pys2'))

#############sorted set#################
# r.zadd('pyz1',{'blue':8000,'wanglaoshi':12000})
# [(b'blue', 8000.0), (b'wanglaoshi', 12000.0)]
# print(r.zrange('pyz1',0,-1,withscores=True))
r.zadd('pyz2',{'blue':6000})
r.zinterstore('pyz3', ('pyz1', 'pyz2'), aggregate='max')
print(r.zrange('pyz3',0,1,withscores=True))
