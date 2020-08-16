# 4.继承threading类
import threading
import time

# 4.1 这样写完全和调用方法是一样的
# class A(object):
#     # def __init__(self):
#     #     pass
#     def demo(self):
#         for i in range(5):
#             print('demo')
#             time.sleep(1)
#
#
# class B(object):
#     def demo1(self):
#         for i in range(5):
#             print('demo1')
#             time.sleep(1)
#
# if __name__ =='__main__':
#     t = threading.Thread(target=A().demo)
#     t1 = threading.Thread(target=B().demo1)
#     t.start()
#     t1.start()

# 4.2 继承threading类
class A(threading.Thread):
    # def __init__(self):
    #     super().__init__()

    def run(self):
        for i in range(5):
            print(i)

    def demo(self):
        for i in range(5):
            print(i)

if __name__ == "__main__":
    t = A()
    t.start()     #继承父类的start,调用run 方法可实现，所以run方法是核心
    t.demo()      # 这种方式不是多线程的方式，需要在run方法调用demo的方法