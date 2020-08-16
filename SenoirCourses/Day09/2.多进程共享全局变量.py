# 2.多进程共享全局变量
# 2.1 多进程不共享全局变量
import multiprocessing
from queue import Queue

# a = 1
#
#
# def demo1():
#     global a
#     a += 1
#
#
# def demo2():
#     # 进程是不共享的， 输出是1，不是2
#     print(a)
#
#
# if __name__ == '__main__':
#     t1 = multiprocessing.Process(target=demo1)
#     t2 = multiprocessing.Process(target=demo2)
#
#     t1.start()
#     t2.start()

# 2.2 队列


def demo1(q):
    # try:
    # 1/0
    q.put('a')
    # except Exception as e:
    #     print(e)


def demo2(q):
    try:
        data = q.get()
        print(data)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 普通队列，不能完成进程间的通信
    q = Queue()                      # 报错
    # q = multiprocessing.Queue()    # 改成跨进程队列输出a
    t1 = multiprocessing.Process(target=demo1, args=(q,))
    t2 = multiprocessing.Process(target=demo2, args=(q,))

    t1.start()   # 报错
    t2.start()

    # t1.run()      # 输出 a
    # t2.run()