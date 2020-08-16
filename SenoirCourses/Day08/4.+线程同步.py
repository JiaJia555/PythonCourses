# 4. 线程同步, condition
'''
天猫精灵:小爱同学
小爱同学:在
天猫精灵:现在几点了？
小爱同学：你猜猜现在几点了
'''

import threading


class XiaiAi(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="小爱同学")
        # self.lock = lock
        self.cond = cond

    def run(self):
        with self.cond:
            print(4)
            self.cond.wait()
            print(5)
            print("{}:在".format(self.name))
            self.cond.notify()

            self.cond.wait()

            print("{}:你猜猜现在几点了".format(self.name))

            self.cond.notify()

        # self.lock.acquire()
        # print("{}:在".format(self.name))
        # self.lock.release()
        #
        # self.lock.acquire()
        # print("{}:你猜猜现在几点了".format(self.name))
        # self.lock.release()


class TianMao(threading.Thread):
    def __init__(self, cond):
        super().__init__(name="天猫精灵")
        # self.lock = lock
        self.cond = cond

    def run(self):
        self.cond.acquire()
        print("{}:小爱同学".format(self.name))
        print(1)
        self.cond.notify()
        print(2)

        self.cond.wait()
        print(3)

        print("{}:现在几点了？".format(self.name))

        self.cond.notify()

        self.cond.wait()

        self.cond.release()

        # self.lock.acquire()
        # print("{}:小爱同学".format(self.name))
        # self.lock.release()
        #
        # self.lock.acquire()
        # print("{}:现在几点了？".format(self.name))
        # self.lock.release()


class Siri(threading.Thread):

    def __init__(self, cond):
        super().__init__(name="Siri")
        # self.lock = lock
        self.cond = cond

    def run(self):
        self.cond.acquire()
        print("{}:小爱同学".format(self.name))

        self.cond.notify()

        self.cond.wait()

        print("{}:现在几点了？".format(self.name))

        self.cond.notify()

        self.cond.wait()

        self.cond.release()



if __name__ == "__main__":
    # mutex = threading.RLock()
    cond = threading.Condition()
    xiaoai = XiaiAi(cond)
    tianmao = TianMao(cond)
    siri = Siri(cond)
    # 启动顺序很重要的
    xiaoai.start()
    tianmao.start()
    siri.start()

'''
输出为：
天猫:小爱同学
天猫:现在几点了？
小爱同学:在
小爱同学:你猜猜现在几点了

每句话加互斥锁也还是相同输出
'''