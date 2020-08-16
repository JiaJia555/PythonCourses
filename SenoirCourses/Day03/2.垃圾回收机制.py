# 2.Python垃圾回收机制
# 当这个对象的引用计数（指针数）为 0 的时候，说明这个对象永不可达，自然它也就成为了垃圾，需要被回收。

import os
import psutil


# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))  # 6.99609375 MB


def func():
    show_memory_info('initial')
    # 函数内部的局部变量，函数运行之前或运行结束之后，该变量无效
    # global a 变成全局变量
    a = [i for i in range(10000000)] # 列表推导式
    show_memory_info('after a created') # 394.01953125 MB
    # return a  # 没有变量接收，最后一个输出为6.99609375 MB


# f = func() # 有变量接收，最后输出394.31640625 MB
print('123')
func()
print('123')
show_memory_info('finished')   # 6.99609375 MB

