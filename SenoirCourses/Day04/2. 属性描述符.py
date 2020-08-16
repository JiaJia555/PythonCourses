# 2. 属性描述符


# class User(object):
#     def __init__(self, age, name):
#         self.age = age
#         self.name = name
#
#     def get_age(self):
#         return self.age
#
#     def set_age(self, age):
#         if not isinstance(age, int):
#             raise TypeError('type error')
#         self.age = age
# 2.1 这个方法是对age一个属性进行验证，如果有多个属性要怎么验证?怎么复用此类方法
# 属性描述符 __get__, __set__, __delete__,统一验证int, str这种类型
# 和Django比较类似
# 下面案例是数据描述符，只要是整数类型的都可以这样做，如果是str类型类似的命名一个str类

class IntField(object):
    """
    数据描述符
    """
    def __get__(self, instance, owner):  # instance 都是类User的一个对象
        print("__get__")
        return self.values

    def __set__(self, instance, value):
        print("__set__")
        # print(instance)    # <__main__.User object at 0x000000089C5FE3C8>
        # print(value)       # 30
        if not isinstance(value, int):
            raise ValueError('Value Error')
        self.values = value

    def __delete__(self, instance):
        pass


class User:
    # age = IntField()
    age = 9


user = User()
# 2.再找user__dict__
# user.__dict__['age'] = 18
# 1.先调用数据描述符的age
user.age = 30          # 赋值之后打印set,
# user.age = "20"      # value Error
print(user.age)        # 打印调用get方法

'''
属性查找顺序

user = User(), 那么user.age 顺序如下:

1 如果"age"是出现在User或其基类的__dict__中, 且age是data descriptor,那么调用其__get__方法, 否则

2 如果"age"出现在user的__dict__中, 那么直接返回 obj.__dict__['age'],否则

3 如果"age"出现在User或其基类的__dict__中

3.1 如果age是non-data descriptor,那么调用其__get__方法， 否则

3.2 返回 __dict__['age']

4 如果User有__getattribute__和__getattr__, 先调用__getattribute__，再调用__getattr__方法，否则

5 抛出AttributeError
'''

# 2.2 非数据描述符,一般不用__set__, 但是也可以用
class NoneDataIntField:
    def __get__(self, instance, owner):
        print('get is called')
        return self.value

    def __set__(self, instance, value):
        print('set is called')
        self.value = value


class D(object):
    name = NoneDataIntField()


d1 = D()
print("给对象d1设置name属性的值")
d1.name = "ddl"                                      # set is called
print("实例数据覆盖了非数据描述符, 不会调用__get__")
print(d1.name)                                       # get is called, ddl




