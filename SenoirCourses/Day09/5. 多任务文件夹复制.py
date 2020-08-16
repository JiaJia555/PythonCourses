# 5.多任务文件夹复制
'''
1. 获取用户要复制的文件夹名字
2. 创建一个新的文件夹
3. 获取文件夹的所有待拷贝的文件名字
4. 创建进程池
5. 添加拷贝任务
'''

import multiprocessing


def main():
    # 获取用户要复制的文件夹名字
    old_folder_name = input("请输入要复制的文件夹名字:")

    # 创建一个新的文件夹
    new_folder_name = old_folder_name + "复件"

