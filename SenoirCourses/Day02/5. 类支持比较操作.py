# @ Time     : 2020/1/2
# @Author    : JiaJia
# 5. 如何让类支持比较操作
from functools import total_ordering
import math
import abc
# 此类方法已经不介意使用了
# from abc import ABCMeta, abstractclassmethod
# class Shape(metaclass=ABCMeta):
#     @abstractclassmethod

@total_ordering
class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):  # 父类可以随便写，因为会强制子类重写父类方法
        pass
    # 把公共方法lt,eq写在这里

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()


class Rect(Shape):  # object改成Shape
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

    # def __str__(self):
    #     return '(%S, %S)' % (self.w, self.h)

    # def __lt__(self, other):
    #     return self.area() < other.area()  # other是比较的那个值
    #
    # def __eq__(self, other):
    #     return self.area() == other.area()


rect1 = Rect(1, 2)
rect2 = Rect(3, 4)

# 加__lt__方法之前会报错，类不能直接比较
print(rect1 > rect2)   # python内部会自动调整为rect2 < rect1,因为只定义了<
# print(rect1 >= rect2) 报错，只可判断==
# 为了可以判断所有的符号，大于小于等于各种组合，import total_ordering, 只要完成lt和 eq
print(rect1 <= rect2)

# 有其他类,如何跨类比较。定义圆的面积，要怎么和长方形比较
class Circle(Shape): # object 需要改成Shape
    def __init__(self, r):
        self.r = r

    def area(self):
        return self.r ** 2 * math.pi

    # def __lt__(self, other):
    #     return self.area() < other.area()
    #
    # def __eq__(self, other):
    #     return self.area() == other.area()


c = Circle(8)
rect = Rect(1, 2)
# 这个方法可以跨类比较，但是很多代码重复，引用抽象基类来简化他,最上面，把重复的代码都写在下面，注释掉单个部分的
print(c == rect)

