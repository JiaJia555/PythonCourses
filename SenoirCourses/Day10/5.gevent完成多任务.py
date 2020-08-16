import gevent
import time
from gevent import monkey
# 将程序中用到的耗时操作  换为gevent中实现的模块
monkey.patch_all()

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)             # gevent 不认识time


def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        # time.sleep(0.5)
        gevent.sleep(0.5)


print("--1--")
g1 = gevent.spawn(f1, 5)
print("--2--")
time.sleep(1)
# gevent.sleep(0.5)
g2 = gevent.spawn(f2, 5)
print("--3--")
g3 = gevent.spawn(f3, 5)
print("--4--")


g1.join()           # 延迟等待
g2.join()
g3.join()