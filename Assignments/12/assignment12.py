# 1. is 与==的区别
'''
==是python标准操作符中的比较操作符，用来比较判断两个对象的value(值)是否相等
is 用于判断 两个变量 引用对象是否为同一个， id是否相同
'''
a = [1,2,3]
b = [1,2,3]
if a == b:
    print("true")
if a is b:
    print("true")
else:
    print("false")
# 2. 可变对象与不可变数据类型分别有哪些？并且区别在哪里？
# 数值（整型，浮点型），布尔型，字符串，元组属于值类型，本身不允许被修改（不可变类型）
# 数值的修改实际上是让变量指向了一个新的对象（新创建的对象），所以不会发生共享内存问题。

# 列表，集合，字典是引用类型，本身允许修改（可变类型）。

# 区别：可变数据类型，允许变量的值发生变化，即如果对变量进行append、+=等这种操作后，
# 只是改变了变量的值，而不会新建一个对象，变量引用的对象的地址也不会变化，不过对于相同的值的不同对象，
# 在内存中则会存在不同的对象，即每个对象都有自己的地址，相当于内存中对于同值的对象保存了多份，
# 这里不存在引用计数，是实实在在的对象。
# 3. __init__方法与__new__方法的区别
'''
__init__是当实例对象创建完成后被调用的，然后设置对象属性的一些初始值。
__new__是在实例创建之前被调用的，因为它的任务就是创建实例然后返回该实例，是个静态方法。
也就是说：__new__方法才是实际意义上的构造函数；而__init__ 方法仅为初始化方法；
'''


class Student(object):
    def __new__(cls, *args, **kwargs):
        print('我是new函数！')  # 这是为了追踪new的执行过程
        print(type(cls))  # 这是为了追踪new的执行过程
        return object.__new__(cls)  # 调用父类的（object）的new方法，返回一个Student实例，这个实例传递给init的self参数

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('我是init')

    def study(self):
        print('我爱学习！')


if __name__ == '__main__':
    s = Student('张三', 25)
    print(s.name)
    print(s.age)
    s.study()

# 4. __del__在什么时候触发？代码结合注释说明
# __del__  只有等到对象全部释放,才会主动触发__del__


class Hobbies(object):
    def __init__(self):
        print('__init__方法被调用')

    def __del__(self):
        print("__del__方法被调用")


h1 = Hobbies()
h = h1
del h1
del h

# 5. 单例模式实现
class Dog(object):
    flag = None # 标志

    # 创建对象 __new__
    def __new__(cls, *args, **kwargs):
        # return super().__new__(cls)
        if cls.flag is None:
            cls.flag = super().__new__(cls)
            return cls.flag
        else:
            return cls.flag


d = Dog()  # d是一个对象 d也是Demo类的一个实例
print(id(d))
d1 = Dog()
print(id(d1))

# 6. 实现urls 与views 反射

