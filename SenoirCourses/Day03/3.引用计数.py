# 3.垃圾回收
# 一般的手动释放内存: del方法，也可以用gc模块，可以手动清除没有引用的对象
import sys
import psutil
import os
import gc
gc.collect() #一般del之后用这个

a = [] # +1
# 3.1引用计数，查看变量的引用次数，该函数本身也算一次,也只算一次
print(sys.getrefcount(a))  # 2


# def func(a):  # +1
      # 1 a = []
      # 2 函数调用
      # 3 函数参数
      # 4 getrefcount
#     print(sys.getrefcount(a)) # 1
# func(a)  # 4 = 2 + 2
b = a
print(sys.getrefcount(a))  # 3

# 3.2 引用次数为0 是垃圾回收启动的充分必要条件吗？ 不是，是充分不必要条件。例子中a,b引用次数不为0也可以用gc.collect垃圾回收
# 循环引用 两个对象，它们互相引用，并且不再被别的对象所引用
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)

    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))  # 6.64453125 MB

def func():
    show_memory_info('initial')
    # a,b是局部变量
    a = [i for i in range(10000000)]
    b = [i for i in range(10000000)]
    show_memory_info('after a, b created') # 782.0 MB
    a.append(b)
    b.append(a)

func()
gc.collect()
# show_memory_info('finished') # 782.0 MB，手动销毁变回 7.65234375 MB
# # 函数执行完毕后，局部变量引用次数为0，但是这里的循环引用a,b引用次数并没有为0，内存没有被释放
# # 手动销毁,gc.collect()

# 3.3 调试内存泄漏
#  objgraph，一个可视化引用关系的包。在这个包中，主要推荐两个函数，第一个是 show_refs()，它可以生成清晰的引用关系图。
import objgraph

a = [1, 2, 3]
b = [4, 5, 6]

a.append(b)
b.append(a)

objgraph.show_refs([a])

# Graph written to C:\WINDOWS\TEMP\objgraph-_nnk5i2i.dot (8 nodes)
# Graph viewer (xdot) and image renderer (dot) not found, not doing anything else
# dot转图片:https://onlineconvertfree.com/zh/

'''
总结
垃圾回收是 Python 自带的机制，用于自动释放不会再用到的内存空间；
引用计数是其中最简单的实现，不过切记，这只是充分非必要条件，因为循环引用需要通过不可达判定，来确定是否可以回收；
Python 的自动回收算法包括标记清除和分代收集，主要针对的是循环引用的垃圾收集；
调试内存泄漏方面， objgraph 是很好的可视化分析工具。
'''

