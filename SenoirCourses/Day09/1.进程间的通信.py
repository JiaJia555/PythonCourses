# 1.进程之间的通信
# 1.1 队列，先进先出
import multiprocessing
from multiprocessing import Queue

# 创建队列 最多存放3条数据
# q = Queue(3)

# 存数据
# q.put(1)
# q.put("jiajia")
# q.put([11, 22])
# 在存放第四条数据时,堵塞
# q.put({"name": "jiajia"})
# q.put_nowait({"name": "jiajia"})         # 直接抛出异常raise Full

'''
    def put(self, obj, block=True, timeout=None):
        assert not self._closed, "Queue {0!r} has been closed".format(self)
        if not self._sem.acquire(block, timeout):
            raise Full
    def put_nowait(self, obj):
        return self.put(obj, False)
Queue.put(item, block=True, timeout=None): 往队列里放数据。
如果满了的话，blocking = False 直接报 Full异常。如果blocking = True，就是等一会，
timeout必须为 0 或正数。None为一直等下去，0为不等，正数n为等待n秒还不能存入，报Full异常。
'''
# print(q.get())           # 1
# print(q.get())           # jiajia
# print(q.get())           # [11, 22]
# print(q.get())         # 堵塞，没有输出
# print(q.get_nowait())    #  raise Empty

# print(q.full())          # 判断队列是否为满
# print(q.empty())         # 空


# 1.2 进程间的通信
def download(q):
    """下载数据"""
    lis = [11, 22, 33]
    for item in lis:
        q.put(item)

    print("下载完成，并且保存到队列中...")


def analysis(q):
    """数据处理"""
    analysis_data = list()
    while True:
        data = q.get()
        # print(data)
        analysis_data.append(data)

        if q.empty():
            break

        print(analysis_data)


def main():
    # 创建一个队列 跨进程通信的队列
    q = multiprocessing.Queue()

    t1 = multiprocessing.Process(target=download, args=(q,))
    t2 = multiprocessing.Process(target=analysis, args=(q,))

    t1.start()
    t2.start()

if __name__ =='__main__':
    main()