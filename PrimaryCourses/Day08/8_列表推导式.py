#1. 迭代器
'''
for 循环基本原理
1.调用了__iter__方法iter() 将数据对象 转为 迭代器
2.迭代器调用__next__方法读取数据
list()
range()
Iterable 可迭代的对象
Iterator 迭代器
isinstance(a,int) 判断a是否为int型
'''
a = 1
print(type(a))
print(isinstance(a,int)) # bool
from collections import Iterable,Iterator
# CTRL+D 赋值当前行
# print(isinstance('abc',(Iterable,str)))   # str 不可变 or 但是有可迭代的方法
# print(isinstance([1,2,3,4],Iterable))
# print(isinstance(range(10),Iterable))
# print(isinstance(123,Iterable)) # False
# print(isinstance({1,2,3,4},Iterable))

'''__next__只能顺延调用，不能往前'''
# for i in "1123":
#     print(i)
'''
可迭代的对象不一定是迭代器
'''
# li = [1,2,3,4]  # Iterable
# print(isinstance(li,Iterator))  # False
# lis = iter(li)  # 迭代器
# print(isinstance(lis,Iterator)) # True
# print(type(lis))    # list_iterator

# print(lis[0])   # 迭代器不支持索引取值  报错
# print(lis.__next__())
# print(lis.__next__())
# print(lis.__next__())
# print(lis.__next__())
# print(lis.__next__()) # 超出范围 StopIteration

# print(next(lis))
# print(next(lis))
# print(next(lis))
# print(next(lis))

# for i in lis:
#     print(i)

'''
迭代器作用:节省内存空间,用多少取多少
'''
# li = [1,2,3,4]
# iter()
#2. 生成器
'''自定义长度的列表'''
# def test(number):
#     n = 0
#     # li = []
#     while n<number:
#         # li.append(n)
#         yield n
#         n += 1
#     # print(li)
#
# res = test(20000)
# print(res)  # generator生成器
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# print(res.__next__())
# for i in res:
#     print(i)

# g = (i for i in range(10))  # generator
# print(g)
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
'''
1.遇到yield(生成器),函数会暂停,将对象返回,下次会继续上次暂停的地方执行
2.return 直接返回信息 退出程序
'''
# def createNums():
#     print("----func start------")
#     a,b = 0,1
#     for i in range(5):
#         # print(b)
#         print("--1--")
#         yield b     # return b
#         print("--2--")
#         a,b = b,a+b
#         print("--3--")
#     print("----func end------")
#
# res = createNums()
# # print(res)
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# print(next(res))
# for i in res:
#     print(i)

# def test1():
#     while True:
#         print("--1--")
#         yield None
#
# def test2():
#     while True:
#         print("--2--")
#         yield None
#
# t1 = test1()
# t2 = test2()
# while True:
#     next(t1)
#     next(t2)

# def test1():
#     a1 = yield "hello"
#     # a1 = "world"
#     yield a1
#
# res = test1()
# print(next(res))
# print(res.send("world"))
# print(next(res))
# for i in res:
#     print(i)
#3. 推导式
'''[0.5,1.0,1.5....9.5,10.0]'''
# step 为整数
# print(list(range(0,10,1)))

# li = []
# for i in range(1,21):
#     i = i/2
#     print(i)
    # li.append(i)

# print(li)

# 列表推导式
# li1 = [i/2 for i in range(1,21)]
# print(li1)

'''生成随机列表10个元素 <0 的数进行平方 生成新的列表'''
# import random
# a = random.randint(-20,10)
# print(a)
# rli = [random.randint(-20,10) for i in range(10)]
# print(rli)
'''
1.map函数拟定返回规则
2.筛选出<0的元素构建新的序列
'''
# def f(x):
#     return x**2
#
# f(2)
# rli2 = map(lambda x:x**2,filter(lambda x:x<0,rli))
# print(list(rli2))

'''
三目运算符
# a = 1
# b = 2
# if b-a>0:
#     print(b-a)
# else:
#     print(a+b)
# print(b-a if b-a>0 else a+b)

'''
# li3 = [i**2 for i in rli if i<0]
# print(li3)
# for i in "123":
#     for j in "abc"

# li4 = [i+j for i in "123" for j in "abc"]
# print(li4)

# dic = {"name":"amy","gender":"female"}
# li5 = [k+":"+v for k,v in dic.items()]
# print(li5)

'''dict字典推导式'''
# li = ["name","age","gender"]
# li1 = ["amy","18","male"]
# dic1 = {0:"name",1:"age"}
# dic2 = {li.index(i):i for i in li}
# print(dic2)

'''随机生成10个1-100之间元素,并且去重(set集合)'''
# s1 = {random.randint(1,100) for i in range(10)}
# print(type(s1))
# print(len(s1))

# s2 = {i for i in range(10)}
# s3 = [i for i in range(10)] # list
# print(s2)
# print(type(s2))

'''没有元组推导式'''
# tu = (i for i in range(3)) # 生成器
# print(tu)
# print(tuple(tu))    # 转为元组数据类型


