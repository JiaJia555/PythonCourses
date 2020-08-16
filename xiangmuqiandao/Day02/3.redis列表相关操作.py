import redis

class ListRedis(object):
    def __init__(self):
        self.r = redis.StrictRedis(host='127.0.0.1',port=6379)
	# 列表设置值
    """return: None"""
    def list_lpush(self, keys, items):
        res = self.r.lpush(keys, items)
        # res = self.r.rpush('common','2')

	# 弹出记录
    def list_lpop(self,keys):
        result = self.r.lpop(keys)
        # res = self.r.rpop('common')
        return result
	# 范围取值
    def list_range(self):
        res = self.r.lrange('common',0,-1)
        print(res)

if __name__ =='__main__':
    l = ListRedis()
    # l.list_lpush('li', '1')
    # 不能传多个值 l.list_lpush('li1', (1,2,3))
    l.list_lpop('li')