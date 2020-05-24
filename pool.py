"""
进程池功能演示
"""

from multiprocessing import Pool
from time import sleep,ctime

# 进程池事件
def worker(msg):
    sleep(2)
    print(ctime(),"--",msg)


# 创建进程池 (此刻进程已经产生)
pool = Pool(4)

# 加入要执行的事件
for i in range(10):
    msg = "Tedu%d"%i
    # 加入进程池
    pool.apply_async(func=worker,args=(msg,))


# 关闭进程池 不能加入新的事件
pool.close()

# 等待事件处理完回收进程池
pool.join()


