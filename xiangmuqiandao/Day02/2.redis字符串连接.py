import redis

# redis.StrictRedis()
# r = redis.Redis(host='127.0.1', port=6379, db=0)        # 默认值，也可不写
# r = redis.Redis()
# print(r)

class StringRedis(object):
    def __init__(self):
        self.r = redis.Redis(host='127.0.0.1', port=6379, db=0)

    # 字符串设置值
    def string_set(self, keys, items):
        """字符串设置值:return: None"""
        res = self.r.set(keys, items)
        # 返回布尔值 True
        print(res)

    # 字符串取值
    def string_get(self, keys):
        result = self.r.get(keys)
        return result

    # 设置多个值
    def string_mset(self,items):
        if isinstance(items, dict):
            res =self.r.mset(items)
            print(res)


    def string_del(self, keys):
        if self.r.exists(keys):
            self.r.delete(keys)
        else:
            raise ValueError("{} is not found".format(keys))
            # return "{} is not found".format(keys)


if __name__ == '__main__':
    s = StringRedis()
    # s.string_set('user', 'jiajia')
    # res = s.string_get('user')
    # print(res)
    # print(type(res))
    # d = {
    #     "user1":"jiajia1",
    #     "user2": "jiajia2"
    # }
    # s.string_mset(d)

    print(s.string_del("user3"))