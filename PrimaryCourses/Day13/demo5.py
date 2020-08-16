'''
sys 与python 解释器进行交互的
sys.argv[0] --》程序本身的路径，运行时传入的参数
sys.version 解释器版本
sys.path 模块搜素路径
sys.exit -->正确退出status = 0, 异常退出 =1
'''
import sys
# print(sys.argv)
# res = sys.argv[1]  # 索引获取值
# if res == 'socool':
#     print("谢谢")

# print(sys.version)
# print(sys.path)
# print(111)
# sys.exit() # 调试代码 异常捕捉
# print(222)

import os
'''
os 操作系统
os.getcwd() 当前工作目录（文件夹）
os.chdir() 改变当前的工作目录
'''
# print(os.getcwd())
# os.chdir('D:\\amy')
# os.makedirs('ChangSha')
# print(os.getcwd())

# os.makedirs('ChangSha\\Food')  # 递归创建多个文件夹（空）
# os.removedirs('ChangSha\\Food')  # 递归删除多个文件夹（空）

# os.mkdir('ChangSha\\Food')  # 系统找不到指定的路径
# os.mkdir('ChangSha') # 创建单个文件夹
# os.mkdir('ChangSha\\Food')  # 在路径ChangSha下创建一个文件夹
# os.rmdir('Food') # 删除一个文件夹
# os.rmdir('ChangSha')

# print(os.path.exists('Happy'))  # 返回布尔值，判断路径是否存在

# print(os.path.join(os.getcwd(), "Happy"))

# dirpath = 'Today\\hello'
# if not os.path.exists(dirpath):
#     os.makedirs(dirpath)

