import time
import threading


def sing():
    for i in range(3):
        print("正在唱歌...%d" % i)
        time.sleep(1)


def dance():
    for i in range(3):
        print("正在跳舞...%d" % i)
        time.sleep(1)


if __name__ == '__main__':
    # sing()
    # dance()
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    t1.start()
    t2.start()  # 主线程  会等到子线程执行结束之后主线程才会结束