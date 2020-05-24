"""
3. 文件拆分，将一个大文件拆分为两份,按照字节数平分。
 上下两个部分分别拆分的一个新文件中。要求使用两个子进程同时拆分
"""

from multiprocessing import Process
import os

filename = "./timg.jpg"
size = os.path.getsize(filename) # 文件大小

# fr = open(filename,'rb')  # 父进程和两个子进程用的是同一套文件偏移量，会相互影响

# 复制上半部分
def top():
    fr = open(filename,'rb') # 系统会分配给一个自己的文件偏移量
    fw = open("top.jpg",'wb')
    n = size // 2
    fw.write(fr.read(n))
    fr.close()
    fw.close()

# 复制下半部分
def bot():
    fr = open(filename, 'rb')
    fw = open("bot.jpg", 'wb')
    # 将fr文件偏移量移动到中间位置
    fr.seek(size//2,0)
    fw.write(fr.read())
    fr.close()
    fw.close()


p1 = Process(target=top)
p2 = Process(target=bot)
p2.start()
p1.start()


p1.join()
p2.join()











