"""
循环创建多个进程
"""
from multiprocessing import Process
from time import sleep
import os
import sys

def th1():
    sys.exit("吃饭进程退出了")  # 执行这一句，进程退出
    sleep(3)
    print("吃饭")
    print(os.getppid(),"--",os.getpid())

def th2():
    sleep(2)
    print("睡觉")
    print(os.getppid(), "--", os.getpid())

def th3():
    sleep(4)
    print("打豆豆")
    print(os.getppid(), "--", os.getpid())

things = [th1,th2,th3]
jobs = []  # 用于存放进程对象
for th in things:
    p = Process(target = th)
    jobs.append(p)
    p.start()

# 三个进程都启动之后，一起回收
for i in jobs:
    i.join()


