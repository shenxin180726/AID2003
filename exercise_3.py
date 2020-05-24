"""
练习２：　使用进程池完成
假设一个文件夹中有大量的文件，现在需要将这个文件夹备份一份，编程完成这件事情。
我们把文件夹中给每个文件的复制作为一个进程池事件对待

提示　：　os.mkdir() 创建文件夹

思路 ：
原有文件夹 --》 创建新文件夹
进程池事件是什么 ： 拷贝每一个文件


练习2 plus ： 在练习2的基础上完成
拷贝的过程中实时显示 拷贝的进度
思路： 总共这个文件夹多大
每时每刻都要知道拷贝了多大
"""

from multiprocessing import Pool,Queue
import os

q = Queue() # 消息队列

# 复制一个文件
def copy_file(filename,old_folder,new_folder):
    """
    :param filename: 要拷贝的文件
           old_folder:要备份的文件夹
           new_folder: 目标文件夹
    :return: None
    """
    fr = open(old_folder+filename,'rb')
    fw = open(new_folder+filename,'wb')
    # 开始拷贝
    while True:
        data = fr.read(1024)
        if not data:
            break
        n = fw.write(data)
        q.put(n) #将拷贝的字节数放入消息队列
    fr.close()
    fw.close()

# 获取文件夹大小
def get_total_size(dir):
    total_size = 0
    for file in os.listdir(dir):
        total_size += os.path.getsize(dir + file) # 累加每个文件大小
    return total_size


# 创建进程池
def main():
    old_folder = "/home/tarena/ftp/" # 要备份的文件夹
    total_size = get_total_size(old_folder) # 获取目录总大小
    new_folder = "/home/tarena/ftp-备份/"
    os.mkdir(new_folder)

    # 创建进程池
    pool = Pool()
    for file in os.listdir(old_folder):
        pool.apply_async(func=copy_file,args=(file,old_folder,new_folder))

    copy_size = 0
    while copy_size < total_size:
        copy_size += q.get() # 已经拷贝的大小
        print("已经拷贝了：%.2f%%"%(copy_size/total_size*100))

    pool.close()
    pool.join()

if __name__ == '__main__':
    main()











