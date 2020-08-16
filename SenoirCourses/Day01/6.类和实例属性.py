'''
六 类属性和实例属性及查找顺序
'''


class A(object):
    name = 'shelley'

    def __init__(self, age):
        self.name = "JiaJia"
        self.age = age


a = A(10)
print(a.name)
print(A.name)
'''
DFS: 深度优先
BFS: 广度优先
C3 算法
'''

'''
class D:
    pass


class B(D):
    pass


class C(D):
    pass


class A(B, C):
    pass


print(A.__mro__)
菱形：顺序为 A B C D
'''

'''
class D:
    pass
class B(D):
    pass
class E:
    pass
class C(E):
    pass
class A(B, C):
    pass

print(A.__mro__)
顺序为 A B D C E
'''

'''
七 python对象的自省机制
常见的函数： dir(), type(), hasattr(), isinstance()
'''
class Person(object):
    name = 'Jiajia'

class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name


user = Student('逻辑教育')
# print(user.__dict__)  # 查看类的属性 {'school_name': '逻辑教育'}
#
# print(dir(user))  # 全部的属性，返回模块的属性列表。
# print(user.name)

a = [1, 2]
# print(a.__dict__)  # 报错 'list' object has no attribute '__dict__'
print(dir(a))
print(list.__dict__)
