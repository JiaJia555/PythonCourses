# @ Time   : 2019/12/31
# @ Author : JiaJia
# 1. 派生内置不可变类型
'''
元组是由__new__方法生成的, init只是初始化值

list('abc')
l = list.__new__(list, 'abc')
l -->输出为[]
list.__init__(1, 'abc')
l -->输出为['a', 'b', 'c']
tuple('abc')
t = tuple.__new__(tuple, 'abc')
t  -->输出为('a', 'b', 'c')
tuple.__init__(t, 'abc')
t  -->输出为('a', 'b', 'c')
'''


class IntTuple(tuple):
    def __init__(self, iterable):
        # for i in iterable: # for 循环
        #     if isinstance(i, int) and i > 0:
        #         super().__init__(i)  # object.__init__() takes exactly one argument (the instance to initialize)
        print(self)  # 输出(2, -2, 'jr', ['x', 'y'], 4)


int_t = IntTuple([2, -2, 'jr', ['x', 'y'], 4])   #  (2,4)
print(int_t)

# self对象到底是谁创建的呢?
# __new__方法创建的

class A(object):
    def __new__(cls, *args, **kwargs):  #创建对象
        print("A.__new__", cls, args)
        return object.__new__(cls)  # 返回值之后__init__才能调用
        # return super().__new__(cls)  # 比较容易混，不介意使用

    def __init__(self, *args):
        print("A.__init__")


# a = A(1, 2) # 等同于下面两个
# a = A.__new__(A, 1, 2)  # 输出为A.__new__ <class '__main__.A'> (1, 2)
# A.__init__(a, 1)  # 输出为 A.__init__

class IntTuple(tuple):
    def __new__(cls, iterable):
        # for i in iterable: # for 循环
        #     if isinstance(i, int) and i > 0:
        #         super().__init__(i)
        # 生成器，和for循环是一样的
        # f = (i for i in iterable if isinstance(i, int) and i > 0)
        f = [i for i in iterable if isinstance(i, int) and i > 0]   # 列表推导式
        print(f)  # f是一个列表
        return super().__new__(cls, f)  # 输出(2, 4)


int_t = IntTuple([2, -2, 'jr', ['x', 'y'], 4])
print(int_t)  # (2,4)

