# @ Time   : 2019/12/31
# @ Author : JiaJia

# 2.如何为创建大量实例节省内存
# 创建多个类，每个类都会产生大量数据占内存。动态属性+ __slots__
import sys
import tracemalloc


class Player1(object):
    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid  # 10.7 MiB
        self.name = name
        self.status = status
        self.level = level


class Player2(object):
    __slots__ = ('uid', 'name', 'status', 'level')  # 关闭动态属性

    def __init__(self, uid, name, status=0, level=1):
        self.uid = uid
        self.name = name
        self.status = status
        self.level = level


p1 = Player1('0001', 'jiajia')
p2 = Player2('0002', 'jiajia1')

# print(dir(p1))
# print(len(dir(p1)))  # 30
# print(dir(p2))
# print(len(dir(p2)))  # 29

# __weakref__ 弱引用
# __dict__ 显示动态绑定属性，浪费的内存
print(set(dir(p1)) - set(dir(p2)))
# 输出为{'__dict__', '__weakref__'}

p1.x = 6
p1.__dict__['y'] = 7
print(p1.__dict__)
# 输出为{'uid': '0001', 'name': 'jiajia', 'status': 0, 'level': 1, 'x': 6, 'y': 7}

# __slots__不允许额外绑定属性，强制绑定会报错
# p2.y = 7 # AttributeError:'Player2' object has no attribute 'y'
# print(p2.name) # 依然可以取值

# 也不可以通过slots外部添加属性，会报错
# p2.__slots__ = ('x') # AttributeError: 'Player2' object attribute '__slots__' is read-only

# 2.1查看内存占用到底是多少，导入模块sys, 使用getsizeof()，只能传入内置的数据类型
# print(sys.getsizeof(p1.__dict__))
# print(sys.getsizeof(p1.name))
# print(sys.getsizeof(p1.uid))

# 2.2
# p1内存应该是是大于p2的，因为p2关闭了动态属性，输出p1小于p2是因为p1没有算上dict 的内存，在第11行
tracemalloc.start()
# p1 = [Player1(1, 2, 3) for _ in range(100000)]  # 1.1 6274 KiB  #  1.2 16.8 MiB
p2 = [Player2(1, 2, 3) for _ in range(100000)]    # 2.1 7837 KiB  # 2.2 7837 KiB
end = tracemalloc.take_snapshot()   # 432 B
# top = end.statistics('lineno')  # 1.同时查看p1,p2占用内存
top = end.statistics('filename')  # 2.分别查看p1,p2每个文件各占用内存

for stat in top[:10]:
    print(stat)







