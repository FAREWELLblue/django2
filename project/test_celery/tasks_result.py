from celery import Celery
#初始化celery, 指定broker
app = Celery('guoxiaonao',
             broker='redis://@127.0.0.1:6379/1',
            backend='redis://@127.0.0.1:6379/2',
             )

#若redis无密码，password可省略
#app = Celery('guoxiaonao', broker='redis://:@127.0.0.1:6379/1')

# 创建任务函数
@app.task
def task_test(a,b):
    print("task is running....")
    return a+b