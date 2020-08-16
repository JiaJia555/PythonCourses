'''
5.线程间通讯--多线程共享全局变量

5.1 修改全局变量一定要加global吗

修改了指向，id变了，就需要加global
+= 是不会修改指向的，但是数据是不可变类型，所以一定会变
a = a+[] 会修改指向
'''
import threading
import time


# num = 100
# lis = [11, 22]
#
# def demo():
#     global num
#     num += 100
#
#
# def demo1():
#     lis.append(33)
#
# def demo2():
#     global lis
#     lis = lis +[44]     # 修改了指向，id变了，就需要加global
#
# print(num)   # 100
# demo()
# print(num)   # 200
# demo1()      # [11, 22, 33]
# # demo2()
# print(lis)

'''
5.2 多线程共享全局变量
'''
num = 100

def demo1():
    global num
    num += 1
    print("demo1---%d" % num)

def demo2():
    print("demo2---%d" % num)


def main():
    t1 = threading.Thread(target=demo1())
    t2 = threading.Thread(target=demo2())
    t1.start()
    time.sleep(1)

    t2.start()
    time.sleep(1)

    print("main---%d" % num)

if __name__ == '__main__':
    main()

'''
5.3 多线程参数
'''
# num = [11,22]
#
#
# def demo1():
#     num.append(33)
#     print("demo1---%s" % str(num))
#
#
# def demo2():
#     print("demo2---%s" % str(num))
#
#
# def main():
#     t1 = threading.Thread(target=demo1(), args=(num,))
#     t2 = threading.Thread(target=demo2(), args=(num,))
#     t1.start()
#     time.sleep(1)
#
#     t2.start()
#     time.sleep(1)
#
#     print("main---%s" % str(num))
#
#
# if __name__ == '__main__':
#     main()
#

