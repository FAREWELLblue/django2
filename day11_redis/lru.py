keys=[]
# 当有key加入
def push(key):
    keys.append(key)
# 当列表中的key调用时
def use(key):
    keys.remove(key)
    push(key)
# 淘汰最少使用的key
def pop():
    del keys[0]
