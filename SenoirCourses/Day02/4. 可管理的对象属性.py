# @ Time     : 2020/1/2
# @Author    : JiaJia
# 4.如何创建可管理的对象属性
'''
麻烦
A.get_key()  #访问器
A.set_key()  #设置器

A.key()
A.key = "jia"
形式上 属性访问
实际上 调用方法
'''

class A:
    def __init__(self, age):
        self.age = age

    def get_age(self):
        return self.age

    def set_age(self, age):
        if not isinstance(age, int):
            raise TypeError('TyprError')
        self.age = age
    # property(fget = None, fset = None, fdel = None. doc = None) -->property attribute
    # R = property(get_age, set_age, )   # 4.2

    @property        # get
    def S(self):
        return self.age

    @S.setter         #set
    def S(self, age):
        if not isinstance(age, int):
            raise TypeError("Type Error")
        self.age = age


a = A(18)
# print(a.age)
# 文件读取的 str
# a.age = '20'
# print(type(a.age))  # <class 'str'>

# 4.1 设置 get_age, set_age 和raise error避免str error
# a.set_age('20')  # 报错
# a.set_age(20)
# print(a.get_age()) # 20

# 4.2 设置属性 property 满足形式上 属性访问 实际上 调用方法
# property 有两种方式，前面是第一种方法，第二种就是@property, @x.setter/deleter 可参考源码
# a.R = 20
# print(a.R)  #其实就是a.age

# 4.3 @property, @x.setter/deleter 取值就会先调用get,赋值就先调用set
a.S = 12
print(a.S)

