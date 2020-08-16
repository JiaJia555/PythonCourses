import redis

class TestHash(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1', port=6379)

    # 批量设值

    def test_hset(self):
        dic = {
            'id': 1,
            'name': 'huawei'
        }
        res = self.r.hmset('mobile', dic)

    # 批量取值

    def test_hgetall(self):
        res = self.r.hgetall('mobile')
    # 判断是否存在
    # 存在返回1
    # 不存在返回0

    def test_hexists(self):
        res = self.r.hexists('mobile', 'id')
        print(res)


if __name__ == "__main__":
    a = TestHash()
    a.test_hset()


# https://blog.csdn.net/qq_43621629/article/details/104745635?fps=1&locationNum=2