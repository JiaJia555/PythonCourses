# 1. 进程
'''
程序：静态的，exe
进程：正在运行的程序，代码+用到的资源
等待->就绪->运行
子进程会整体复制全部代码再执行一遍，造成资源浪费
'''
'''
进程：能够完成多任务，一台电脑上可以同时运行多个QQ
线程：能够完成多任务，一个QQ中的多个聊天窗口
根本区别：进程是操作系统资源分配的基本单位，而线程是任务调度和执行的基本单位
'''
import threading
import time
import multiprocessing
import os


# def demo():
#     while True:
#         print("--1--")
#         time.sleep(1)
#
#
# def demo1():
#     while True:
#         print("--2--")
#
#
# def main():
#     # t1 = threading.Thread(target=demo)
#     # t2 = threading.Thread(target=demo1)
#     p1= multiprocessing.Process(target= demo)
#     p2 = multiprocessing.Process(target=demo1)
#
#     p1.start()
#     p2.start()
#
#
# if __name__ == '__main__':
#     main()

# pid = os.fork()
# print("jiajia")
#
# # pid == 0 子进程
# if pid ==0:
#     print("子进程:{}, 父进程:{}".format(os.getpid(), os.getppidd()))
# else:
#     print("父进程:{}".format(os.getpid()))
#
# time.sleep(2)

'''
jiajia
f_fork:2280
jiajia
s_fork:2281,f_fork:2280
'''
