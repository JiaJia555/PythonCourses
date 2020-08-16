# 1.线程
import threading
import time


# def demo():
#     print("hello World")
#     time.sleep(1)
#
# if __name__ == "__main__":
#     for i in range(5):
#         t = threading.Thread(target=demo)
#         t.start()

# 1.1 主线程  会等到子线程执行结束之后主线程才会结束
def demo1():
    print("demo1")


def demo():
    for i in range(5):
        print("hello World")
        time.sleep(1)
        t1 = threading.Thread(target=demo1)
        t1.start()


if __name__ == "__main__":
    t = threading.Thread(target=demo)
    # t.setDaemon(True)  # 守护线程 不会等子线程结束 直接输出hello world, 1结束
    t.start()
    # t.join()  # 等待子线程执行结束 主线程继续执行，全部输出完毕最后输出1
    print(1)