#1. *args,**keargs 参数是什么？
'''python中规定参数前带 * 的，称为可变位置参数，通常称这个可变位置参数为*args。
*args：是一个元组，传入的参数会被放进元组里。
python中规定参数前 带 ** 的，称为可变关键字参数，通常用**kwargs表示。
**kwargs：是一个字典，传入的参数以键值对的形式存放到字典里。'''
# def add(*args):
#     sum = 0
#     for i in args:
#         sum = sum + i
#     print(sum)
# add(1,2,4)
#
# def dic(**kwargs):
#     print(kwargs)
# dic(x=1, y=2)
#2. 求1-100 的累加(使用到匿名函数以及reduce 方法)
# from functools import reduce
# print(reduce(lambda x,y: x+y, range(1,101)))

#print(sum(range(1,101)))

#3. 将该列表l = ["jack", ("tom", 23), "rose", (14, 55, 67)]中的元素全部遍历出来
# (注意奥!其中可以用到isinstance()方法,大家请自行查阅)
l = ["jack 123", ("tom", 23), "rose", (14, 55, 67)]
#print (*l, sep='\n')
# def dp(s):
#     if isinstance(s, (int,str)):
#         print(s)
#     else:
#         for item in s:
#             dp(item)
# dp(l)

#4. 将以下列表li = [-11,1,-1,-6,5,8]的负值全部变为正数(注意:可以用到map 函数)
# li = [-11,1,-1,-6,5,8]
# res = (map(abs, li))
# lis = list(res)
# print (lis)

#5. 以下列表li = [1,5,11,22,13,50,12]筛选大于10 的数
# res= list(filter(lambda x:x>10,[1,5,11,22,13,50,12]))
# print(res)
# li = [1,5,11,22,13,50,12]
# def is_odd(x):
#     if x >10:
#         return x
# res = filter(is_odd, li)
# print(list(res))

#6. 满足哪几个条件形成一个闭包?
# 1)必须有一个内嵌函数
# 2)内嵌函数必须引用外部函数中的变量
# 3)外部函数的返回值必须是内嵌函数
#7. 实现为增加商品函数添加是否登录正确的判断功能,当为登录状态
#时,则直接打印输出添加商品,否则,让用户登录,判断用户输入的用户
#名以及密码是否正确，如正确则登录,否则提醒用户输入错误。并且
#不能添加。
#7.闭包装饰器
# FLAG = False
# def outer(func):
#     def inner():
#         global FLAG
#         if FLAG:
#             func()
#         else:
#             username = input("请输入用户名:")
#             password = input("请输入用户密码:")
#             if username == 'amy' and password == "123456":
#                 FLAG = True
#                 func()
#             else:
#                 print("用户名或密码错误,登录失败")
#     return inner
#
# @outer
# def shoplist_add():
#     print("增加一件商品")
#
# add_goods = outer(shoplist_add)     # add_goods = inner
#
# shoplist_add()




