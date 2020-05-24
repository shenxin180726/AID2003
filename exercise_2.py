"""
练习1： 大于1的整数，只能被1和他本身整除
一个进程： 写一个函数 求100000以内质数之和 ，计算一下所用的时间

4个进程 求100000以内质数之和 1---25000  25001--50000 50001---75000  75001-10000
计算时间

10个进程 求100000以内质数之和
"""
from multiprocessing import Process
import time

# 求函数执行时间的装饰器
def timeis(f):
    def wrapper(*args,**kwargs):
        start_time = time.time()
        res = f(*args,**kwargs)
        end_time = time.time()
        print("函数执行时间：",end_time - start_time)
        return res
    return wrapper



# 判断一个数是质数
def isPrime(n):
    """
    :param n: 一个数字
    :return: 是质数返回True  不是返回False
    """
    if n <=1 :
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    return True

class Prime(Process):
    def __init__(self,begin,end):
        """
        :param begin: 从哪个数开始
        :param end: 到那个数结尾
        """
        self.begin = begin
        self.end = end
        super().__init__()

    def run(self):
        prime = []
        for i in range(self.begin,self.end):
            if isPrime(i):
                prime.append(i)
        print(sum(prime))

# 100000以内质数之和
# @timeis
# def process_1():
#     prime = []
#     for i in range(100001):
#         if isPrime(i):
#             prime.append(i) # 质数添加到一个列表中
#     print(sum(prime))


# process_1() # 函数执行时间： 33.78674674034119

# @timeis
# def process_4():
#     jobs = []
#     for i in range(1,100001,25000):
#         p = Prime(i,i+25000)
#         jobs.append(p)
#         p.start()
#     for i in jobs:
#         i.join()
#
# process_4()  # 函数执行时间： 24.917572021484375

@timeis
def process_10():
    jobs = []
    for i in range(1,100001,10000):
        p = Prime(i,i+10000)
        jobs.append(p)
        p.start()
    for i in jobs:
        i.join()

process_10()  # 函数执行时间： 22.818427801132202