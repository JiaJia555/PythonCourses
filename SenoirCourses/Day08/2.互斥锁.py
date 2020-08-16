import threading
import time

num = 0
# 创建一个互斥锁，默认是没有上锁的
# mutex = threading.Lock()  # 每一个程序只能加一个锁，加两个会报错
mutex = threading.RLock()   # 可重入的锁，可加多个锁

def demo1(nums):
    global num
    # 加锁
    mutex.acquire()
    mutex.acquire()
    for i in range(nums):
        num += 1
    # 解锁
    mutex.release()
    mutex.release()
    print('demo1---num:%d' % num)


def demo2(nums):
    global num
    # 加锁
    mutex.acquire()
    for i in range(nums):
        num += 1
    # 解锁
    mutex.release()
    print('demo2--num:%d' % num)


def main():
    t1 = threading.Thread(target=demo1, args=(1000000,))
    t2 = threading.Thread(target=demo1, args=(1000000,))

    t1.start()
    t2.start()

    time.sleep(1)  # 这时就会输出 2000000
    print("main---num:%d" % num)

if __name__ == '__main__':
    main()
'''
main---num:392591      # 主线程会等待子线程执行，子线程执行的时候主线程也会继续向下执行
demo1---num:1000000
demo1---num:2000000
'''