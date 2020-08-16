'''
异常
try:
    正常程序
except:
     抛出错误时执行的代码块
'''

# while True:
#     try:
#         ipt = input('请输入')
#         i = float(ipt)
#     except Exception as e: # e = Exception()
#         '''
#         # e 是exception 对象，对象中封装了错误信息
#         #上述代码如果出错，自动执行当前代码
#         '''
#         print(e)
#         i = 1
#         print(i)

# li = [1, 2, 3]
# li[3]  # IndexError
# li[:10]  # 不会报错，默认取出最后一个

# a = 1
# b = 0
# c = a/b  # division by zero

# int('a') # ValueError
# print (dir(__builtins__))  # 问题, ipython报错，找不到builtin
'''
以上细分的错误都是Exception的子类
细分错误的作用:为了一个种类的错误记录日志
为了避免程序最后报错,在最后可以用到Exception捕获异常
如果有错,执行except里的代码块
如果没有错误,执行else
finally:不管处不出错,肯定执行
'''
# try:
#     int('a')
#     # int(1)
# except ValueError as e:  # e = ValueError()
#     print ("ValueError", e)
#     # print(e)
# except ZeroDivisionError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print('没有错误，请执行我')
# finally:
#     print("不管出不出错，都要执行")
'''
raise Exceptions(msg)
'''
# try:
#      int('a')
#      raise Exception('我生气了！')
# except Exception as e:
#     print(e)

# def demo():
#     return False
# def demo1():
#     try:
#         int('a')
#         res = demo()
#         if not res: # True
#             # 打开文件。写日志
#             raise Exception ('demo中有错误')
#     except Exception as e:
#         print(e)

# class OldAmyError(Exception):
#     def __init__(self, msg):  #形参，传送错误信息
#         self.error_info = msg
#
#     def __str__(self):
#         return self.error_info

# err = OldAmyError('咖啡说我是胖子')
# print(err)

# try:
#     raise OldAmyError("咖啡说我是胖子")  # err = OldAmyError("咖啡说我是胖子")
# except OldAmyError as e:
#     print(e)

'''
断言: assert 条件
如果条件成立，代码继续往下执行
如果条件不成立，直接抛出异常
强制用户服从，可捕获但不捕获
'''
# print(123)
# # assert 1 == 2  # AssertionError
# assert 2.0 == 2
# print(456)

'''
模块 提高代码的维护性
1. import xxx  # 模块名，方法
2. from xxx import name1, name2 # name1()
3. from xxx import *  # name1()
4. from xxx import name1 ad demo3_name1  # demo3_name1

as 仅是重命名  # 解决命名冲突
'''









