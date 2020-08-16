# if True:
#     a = 5
#
# print(a)
#
# for i in range(3):
#     print('hello world')
#
# print(i)            # 2
#
#
# def test():
#     # 局部变量 只能在函数体内部使用
#     b = 5
#     return b
#
#
# b = test()      # 5
# print(b)        #  name 'b' is not defined

# a = 200           # global
#
#
# def test1():
#     print('test1:', a)
#
#
# def test2():
#     a = 300
#     print("test2:", a)
#
#
# test1()             # a is not defined
# test2()
# # 先在函数内部找，找不到在外面找
#
# # 函数未调用时，载入内存，优先同级寻找
# c = 10
# def test3():
#     c = 5
#     print(c)            # 先找局部变量
#
#
# test3()     # 5
# print(c)    # 10

# LEGB
a = int(3.14)           # built-in
b = 11                  # global


def outer():
    # global count
    count = 10      # enclosing 嵌套的父级函数的局部作用域
    def inner():
        nonlocal count          # local 局部作用域
        count = 20
    inner()


outer()

'''
LEGB含义解释：
L —— Local(function)；函数内的名字空间
E —— Enclosing function locals；外部嵌套函数的名字空间(例如closure)
G —— Global(module)；函数定义所在模块（文件）的名字空间
B —— Builtin(Python)；Python内置模块的名字空间
'''