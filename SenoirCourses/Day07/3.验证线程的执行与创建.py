'''
3. 验证线程的执行与创建
'''
import threading
import time


def demo():
    for i in range(5):
        print("demo")


def main():
    print(threading.enumerate())
    # 不会创建线程
    t1 = threading.Thread(target=demo)

    print(threading.enumerate())

    # 创建线程并执行
    t1.start()

    print(threading.enumerate())


if __name__ == "__main__":
    main()