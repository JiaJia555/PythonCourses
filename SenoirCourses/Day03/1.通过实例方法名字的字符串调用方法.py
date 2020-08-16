# 1.通过实例方法名字的字符串调用方法, 通过字符串调用方法

from lib_triangle import Triangle
from lib_rectangle import Rectangle
from lib_circle import Circle

shape1 = Triangle(3, 4, 5)
shape2 = Rectangle(4, 6)
shape3 = Circle(1)


def get_area(shape):  # shape传进来的是实例化shape的对象
    method_name = ['get_area', 'getArea', 'area']
    for name in method_name:
        f = getattr(shape, name, None)
        if f:
            return f()


print(get_area(shape1))
print(get_area(shape2))  # 24
print(get_area(shape3))

shape_list = [shape1, shape2, shape3]
area_list = list(map(get_area, shape_list))
print(area_list)  # [6.0, 24, 3.14159]

# 复习1 find()
'''
s = "abc123"
s.find('123')
# 输出3
getattr(s, 'find')
# 输出<function str.find>
getattr(s, 'find')('123')
# 输出3
getattr(s, 'pop')
# 报错，‘str’ object has no attribute 'pop'
getattr(s, 'pop', None) # 没有报错，列表有这个属性
'''
# 复习2 map()
'''
def demo(x):
    return x**2
list(map(demo, [1, 2,3 ]))
'''


