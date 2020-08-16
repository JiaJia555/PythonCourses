# 4.进程池间的通信
import multiprocessing


def demo1(q):
    # 进程池里面的进程 如果出现异常 不会主动抛出
    try:
        print(1)
        q.put('a')
    except Exception as e:
        print(e)


def demo2(q):
    try:
        print(2)
        data = q.get()
        print(data)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    # 进程间的通信
    # q = Queue()       # 不能完成进程之间的通信
    # q = multiprocessing.Queue()      # 进程间的通信
    q = multiprocessing.Manager().Queue()    #进程池中的进程通信

    po = multiprocessing.Pool(2)

    po.apply_async(demo1, args=(q,))
    po.apply_async(demo2, args=(q,))

    po.close()
    po.join()