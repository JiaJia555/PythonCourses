#看视频
'''
01.__doc__ """"""  打印我们类的注释文档
'''
# str()
# print(str().__doc__)

# class Demo(object):
#     # """
#     # 我是demo的注释
#     # """
#     # '我有一个构造方法'
#     # "我....."
#     def __init__(self):
#         pass
#
# d = Demo()
# print(d.__doc__)

'''
__del__  只有等到对象全部释放,才会主动触发__del__
'''
# class Demo:
#     def __del__(self):
#         print("好惨，我被回收了")
#
# d = Demo()
# d1 = d
# print("-"*20)
# del d
# del d1
# print("-"*20)

'''
__call__ 一个实例 也可以变成一个可调用的对象
'''

# class Demo(object):
#     def __call__(self, *args, **kwargs):
#         print("我可以调用了哟")
#
#
# d = Demo()
# d() # 'Demo' object is not callable #问题
# str()

'''
__dict__查看类或者对象的成员 字典
__dict__更像__dir__的一个子集
'''
# class Demo(object):
#     gender = "female"
#     def __init__(self):
#         self.name = "amy"
#         self.__age = 18
#
#     def test(self):
#         print("test")
#
# d = Demo()
# d.test()
# print(d.__dict__)   # dict 查看对象中的实例属性
# print(Demo.__dict__)    # 字典，查看类中的成员-->类属性与行为
# print(d.__dir__())  # 列表 查看对象的-->成员
# print(Demo.__dir__(d)) #对象的 __dir__ 方法用于列出该对象内部的所有属性（包括方法）名，该方法将会返回包含所有属性（方法）名的序列。
# print(d._Demo__age)

'''
02 new 方法
__new__在类准备自身实例化时调用的
__new__ 静态方法 创建对象
__init__实例方法 对象自动调用的方法
'''
# class Demo(object):
#     def __init__(self):
#         print("__init__") # 2
#
#     # 如果我们这个类中没有new,会创建对象时候,会自动执行父类中的new方法
#     def __new__(cls, *args, **kwargs):
#         # print("__new__") # 1
#         return super().__new__(cls) # 传入别的类名时,不会调用__init__方法
#
# d = Demo()
# # 1.创建对象 __new__
# # 2.调用__init__方法
# # 3.返回对象引用

'''
03.单例模式 永远只使用一份对象 (重点:记录日志logger)
1.当对象不存在的时候-->创建对象
2.对象存在-->永远只返回当前已创建对象
'''
# class Demo(object):
#     flag = None # 标志
#
#     # 创建对象 __new__
#     def __new__(cls, *args, **kwargs):
#         # return super().__new__(cls)
#         if cls.flag is None:
#             cls.flag = super().__new__(cls)
#             return cls.flag
#         else:
#             return cls.flag
#
#
# d = Demo()  # d是一个对象 d也是Demo类的一个实例
# print(id(d))
# d1 = Demo()
# print(id(d1))

'''
04. reflect反射
'''

# def func():
#     print("这是一个函数")
#
#
# s = func
# s()  # 'str' object is not callable

# 登录 注册 主页 url映射








