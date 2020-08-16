'''
b
'''

# b = bytes(2)
# print(b)
# b = bytes('')
# f = open('test2.txt', 'wb')
# f.write(b'sjhjjakdh')
# f.write(b)
# print(f.tell())
# f.close()


import time
# f = open('test2.txt', 'w', encoding='utf8')
# f.write('hello 回忆') # 数据一直在内存
# f.close()  #  硬盘
# time.sleep(4)

'''
当报错的时候 f.close()
捕捉异常
'''
# try:
#     f = open('test2.txt', 'w', encoding='utf8')
#     f.write('hello 回忆')  # 数据一直在内存
# finally:
#     if f:
#         f.close()

'''
with 语句自动调用f.close()
with open() as f 上下文管理器
__enter__()
__exit__()
'''
with open('test2.txt', 'r') as f:  # f= open('test2.txt', 'r')
    print(f.read())






