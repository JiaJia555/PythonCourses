'''
三 抽象基类(abc模块)
两个特点：1.不能被实例化 2. 子类方法需要重写
两个应用场景: 1. 判断某个对象的类型
'''


class Demo(object):
    def __init__(self, names):
        self.names = names

    def __len__(self):
        return len(self.names)

    def test(self):
        pass


d = Demo(['juran', 'python'])
print(len(d)) # 输出2
len(d) # 没有任何输出
print(hasattr(d, '__len__'))  # True
print(hasattr(d, '__iter__'))  # False


from collections.abc import Sized

print(isinstance(1, int))  # isinstance 判断对象的类型
print(hasattr(d, 'test'))
print(isinstance(d, Sized))  # 没有len方法时输出False

'''
2. 我们需要强制某个子类必须实现某些方法
web cache redis memcache
'''
import abc


class CacheBase(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get(self, key):
        # raise ValueError
        self.key = key  # 不会报错
    @abc.abstractmethod
    def set(self, key, value):
        # raise NotADirectoryError
        pass


class RedisBase(CacheBase):
    # 重写父类的方法
    def get(self, key):
        pass

    def set(self, key, value):
        pass


r = RedisBase()
r.get("jiajia")   # 子类没有set方法时，第一次报错
