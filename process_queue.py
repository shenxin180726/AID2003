"""
消息队列演示
"""

from multiprocessing import Process,Queue
from time import sleep

# 任何一个进程只要有这个q就可以存取消息，先放入的消息被先取出来
q = Queue(5) # 创建消息队列 需要在父进程中创建，子进程直接使用

def request():
    for i in range(3):
        sleep(2)
        q.put({'name':'张三','age':18})

def handle():
    while True:
        data = q.get()
        print(data)

p1 = Process(target=request)
p2 = Process(target=handle)
p1.start()
p2.start()
p1.join()
p2.join()


