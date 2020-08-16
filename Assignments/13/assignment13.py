# 1.我们继续玩无聊的游戏(猜数字...别敲我)
# 但是我们需要的优化是：
# 1.猜1-10 之间的数,一旦超出10 或者小于0 的数字抛出自定义异常并且捕捉
# 该异常。(eg:MoreThanRangeError...)
# 2.如果输入非数字,捕捉异常,输出异常信息,并且跳出当前循环进入下次循
# 环。
# 3.当输入1-10 之间的数值时,没猜中则提示：没猜对，重新输入。
# 4.猜对了则恭喜。
# import random
#
# class MoreThanTen(Exception):
#     def __init__(self, msg):
#         self.error_info = msg
#     def __str__(self):
#         return self.error_info
# # obj = MoreThanTen('超出范围的异常')
# # print(obj)
#
# class GuessNum(object):
#     def __init__(self):
#         # 注意： 不是左闭右开的
#         self.__num = random.randint(1,10)
#         print(self.__num)
#     def guess_it(self):
#         while True:
#             try:
#                 ipt_num = int(input('输入1-10的数'))
#
#                 if ipt_num > 10 or ipt_num < 0:
#                     raise MoreThanTen('MoreThanRangeError...')
#
#             except MoreThanTen as e:
#                 print(e)
#             except Exception as e:
#                 print('invalid literal for int() with base 10:')
#             if 0 < ipt_num < 11:
#                 if ipt_num == self.__num:
#                     print("猜对了")
#                 else:
#                     print("猜错了")
#
#
# num = GuessNum()
# num.guess_it()

# 2. 导入模块的4 种方式，解决命名冲突。代码演示。
# 1. import xxx  # 模块名，方法
# 2. from xxx import name1, name2 # name1()
# 3. from xxx import *  # name1()
# 4. from xxx import name1 ad demo3_name1  # demo3_name1
# 3. 模块的搜索路径是什么？
import datetime
import sys
print(sys.path)

# 4. 当文件夹不存在时,创建文件夹,否则提示说该文件夹已存在。
import os
# dirpath = 'Today\\hello'
# if not os.path.exists(dirpath):
#     os.makedirs(dirpath)
# os.removedirs('Today\\hello')

# 5. 用os 模块查找当前文件夹下最新创建的文件，该题目需要用到上
# 课时一些没讲到的方法。比如os.listdir(),os.path.getmtime()。大家请
# 自行查阅。
import time
def new_file(testdir):
    # 列出目录下所有的文件
    list = os.listdir(testdir)
    # 对所有文件修改时间进行升序排列
    list.sort(key=lambda fn:os.path.getmtime(testdir + '\\'+ fn))
    # 获取最新修改时间的文件
    filetime = datetime.datetime.fromtimestamp(os.path.getmtime(testdir + list[-1]))
    # 获取文件所在目录
    filepath = os.path.join(testdir, list[-1])
    print('最新修改的文件夹:' + list[-1])
    print('时间：'+ filetime.strftime('%Y-%m-%d %H-%M-%S'))
    return filepath
print(new_file(u"c:\\Windows\\"))



























