from greenlet import greenlet
import time

# 协程利用程序的IO阻塞 来切换任务
def demo1():
    while True:
        print("demo1")
        gr2.switch()
        time.sleep(0.5)


def demo2():
    while True:
        print("demo2")
        gr1.switch()
        time.sleep(0.5)


gr1 = greenlet(demo1)
# print(greenlet.__doc__)
gr2 = greenlet(demo2)

gr1.switch()

