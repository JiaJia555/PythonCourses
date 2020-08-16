import redis

class TestSet(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379)

    # 添加数据
    def test_sadd(self,keys, value):
            res = self.r.sadd(keys, value)

    # 列表添加数据
    def test_sadd2(self, keys,lis):
        for i in lis:
            res = self.r.sadd(keys, i)
    # 删除数据

    # def test_del(self):
    #     res = self.r.srem('set01', 1)

    # 随机删除数据

    # def test_pop(self):
    #     res = self.r.spop('set02')


if __name__ == '__main__':
    res = TestSet ()
    """添加数据"""
    print("\n添加数据")
    res.test_sadd('set1',2)