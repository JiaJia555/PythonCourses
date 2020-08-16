from multiprocessing import Pool

import os, time, random


def worker(msg):
    t_start = time.time()
    print('%s开始执行,进程号为%d' % (msg, os.getpid()))

    time.sleep(random.random() * 2)
    t_stop = time.time()
    # 0.2f 显示两位小数
    print(msg, "执行完成,耗时%0.2f" % (t_stop - t_start))


def demo():
    pass


if __name__ == '__main__':
    po = Pool(3)  # 定义一个进程池  3个进程
    for i in range(0, 10):
        po.apply_async(worker, (i,))   # 添加10个任务 元组，参数

    print("--start--")
    # 关闭进程池 不再接收新的请求 并不是完全关闭 只是改变了状态
    po.close()
    # po.apply_async(demo) # 抛出异常，因为进程池已经关闭了

    # 等待子进程执行完成
    po.join()
    print("--end--")
