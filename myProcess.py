"""
自定义进程类
"""
from multiprocessing import Process

class MyProcess(Process):
    def __init__(self,value):
        self.value = value
        super().__init__() # 执行父类init  有了父类属性

    def fun1(self):
        print("步骤1",self.value)

    def fun2(self):
        print("步骤2")

    # 与start结合，最近进程的启动函数
    def run(self):
        if self.value == 1:
            self.fun1()
        elif self.value == 2 :
            self.fun2()


p = MyProcess(2)
p.start() # 创建进程  自动的运行run方法，将其作为进程执行
p.join()









