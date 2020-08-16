'''
open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
file -->路径
mode -->模式(r w a)
r 只读
w 写入
a append 追加
encoding -->指定编码
'''
# gbk--> 中国码
# utf8-->万国码
f = open("haizi.text", 'r', encoding='utf-8')  # 文件不存在，报错
# print(f.readable()) # 判断是否可读，返回布尔值bool
# print(f.read()) # 读取全部
# print(f.read(13)) # 如果已读全部，接着上面的继续读 f.read(size) size-->字节

# print(f.tell())   # 当前文件指针在文件中的位置
# # print(f.readline())  # 逐行读取 \n. 输出一行空行
# print(f.readline(), end='')  # 换行占两个字节，没有空行了
# print(f.tell())

# print(f.readline(48)) # limited 只读取当前行 13
# print(f.readlines())  # 读取全部 返回列表
# print(f.readlines(12))  # 一行一行读取
'''
第7行加 amy
'''
# content = f.readlines()
# for i in range(len(content)):
#     content[i].strip()
#     if i ==6:
#         print(content[i], 'Amy', end='', sep='')
#     else:
#         print(content[i], end='')
'''
f.read  读取全部
f.readline 逐行读取
f.readlines  输出的是列表
'''













