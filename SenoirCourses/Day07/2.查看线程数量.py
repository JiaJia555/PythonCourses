import threading
import time


def demo1():
    for i in range(5):
        print("--demo1--%d" % i)
        time.sleep(1)
        # break


def demo2():
    for i in range(7):
        print("--demo2--%d" % i)
        time.sleep(1)


def main():
    t1 = threading.Thread(target=demo1)
    t2 = threading.Thread(target=demo2)

    t1.start()
    # time.sleep(1)

    t2.start()
    # time.sleep(1)
    # 获取当前程序所有线程, 同一级棒
    while True:
        print(threading.enumerate())
        if len(threading.enumerate()) <= 1:
            break
        time.sleep(1)
    # [<_MainThread(MainThread, started 6876)>, <Thread(Thread-1, started 6688)>, <Thread(Thread-2, started 4324)>]

if __name__ == '__main__':
    main()