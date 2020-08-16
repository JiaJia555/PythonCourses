#看视频
#super(Son, self) 当前类的名字/ 走神，公有方法是什么来着
#不同根，左边优先。同根，左边没有找右边再找根
#多态，既做参数又做对象

#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
封装:将属性和方法放到类的内部,通过对象访问属性或者方法
'''
# class Demo:
#     def __init__(self):
#         self.name = "amy"
#         self.age = 18
#
#     def print_info(self):
#         print(self.name, self.age)
#
# d = Demo()
# d.print_info()
'''
继承:创建新类的方式,新类可以继承一个或者多个父类
作用:就是避免重复造轮子
新式类 继承object
经典类 不继承object
'''
# class Father(object):
#     pass
# class Son:
#     pass
# f = Father()
# #print(len(f.__dir__()))
#
# s = Son()
# #print(len(s.__dir__()))
#
# class GrandFather(object):
#     def sleep(self):
#         print("睡10个小时")
# class Father(GrandFather):  # 父类 基类
#     def run(self):
#         print("我会跑")
#
#     def eat(self):
#         print("我会吃")
#
# class Son(Father):  # 子类 派生类
#     def study_python(self):
#         print("我学python")
#
#
# s = Son()
# 子类没有 就往父类去找
# s.run()
# s.study_python()
# 父类没有 就会往父类的父类中去找
# s.sleep()
# s.drink()

'''
重写的同时并且执行父类中的方法
'''
# class GrandFather(object):
#     def sleep(self):
#         print("睡10个小时")
# class Farther(GrandFather): #父类 基类
#     def run(self):
#         print("我会跑")
#
#     def eat(self):
#             print("我会吃")
#
# class Son(Father):  # 子类 派生类
#     def study_python(self):
#         print("我学python")
#
#     def sleep(self):  # 重写
#         print("我睡8个小时")
#         # super(Son,self).sleep()
#         super().sleep()
#         # GrandFather.sleep(self) # 类名调用自己创建的self 因为父类的该对象也应该是s
#
# s = Son()
# s.sleep()
'''
总结:
1.继承机制 深度优先 先从自己找 自己找不到 就往父类找
2.重写 防止执行父类的该方法
3.self 都指当前实例化的对象
4.既想要继承父类当中方法 又想拓展新的东西
4.1 super(cls,self).父类中的方法(para)
4.2 父类名.父类中的方法(self,para)
'''

'''
__init__
'''
# class Father(object):
#     def __init__(self):
#         print("Father")
#
# class Son(Father):
#     def __init__(self):
#         print("Son")
#         super().__init__()
#     # pass
#
# s = Son()

# class Father(object):
#     def __init__(self):
#         self.name = "amy"
#         self.__age = 18
#
#     def __test(self):
#         print("__test")
#
#     def test1(self):
#         print(self.__age)
#
#
# class Son(Father):
#     # def __init__(self):
#     #     print("Son")
#     #     super().__init__()
#     def test3(self):
#         # print(self.__age)
#         self.__test()
#
#     def __test(self):
#         print("__test")
#
#
# s = Son()
# print(s.name)
# # print(s.__age)  # 私有属性不会被继承
# # s.__test()  #私有方法不会被继承
# #s.test1()
# s.test3()

'''
如果调用的是继承的父类中的方法，可以在这个公有方法中访问父类中的私有属性和私有方法

但是如果在子类中实现了一个公有方法，那么这个方法是不能够调用继承的父类中的私有方法和私有属性的
'''
'''
多继承
1.左边优先
2.当左边父类的父类,有该方法。右边父类有该方法。左边一条路走到底
3.他们有一个根 根最后才执行
'''
# class GrandFather(object):
#     def sleep(self):
#         print("GrandF睡觉")
#
# class Father(GrandFather):
#     def run(self):
#         print("Father会跑")
#
# class Father1(object):
#     def run(self):
#         print("Father1会跑")
#
#     def sleep(self):
#         print("Father1睡觉")
#
#
# class Son(Father,Father1):
#     pass
#
# s = Son()
# s.run()
# s.sleep()   # C3
# print(Son.__mro__)

# import socketserver
# obj = socketserver.ThreadingTCPServer()
# obj.serve_forever()

#多态
# class Person(object):
#     def print_info(self):
#         print("我是个人")
#
# class Girl(Person):
#     def print_info(self):
#         print("我是amy")
#
# def info(travel):
#     travel.print_info()
#
#
# amy = Person()
# info(amy)
# # amy.print_info()
#
# amy1 = Girl()
# info(amy1)
