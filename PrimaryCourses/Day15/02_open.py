'''
w如果文件不存在 创建文件
'''

f = open('text.txt', 'w', encoding='utf8')
# print(f.writable())
# print(f.write('hello world'))  # 11 写入(字符串) 返回值是字符的长度
# f.write('hello amy')  # 每次写入都会覆盖之前的

# f.writelines(['hello one\n', 'hello two \n', '你好'])
'''
a 追加
+ 可读可写
r+
w+
'''
# f = open('test1.txt', 'a')
# f.write('hello bruin')

# f = open('test1.txt' 'r') # not writable
# f = open('test1.txt', 'r+') # 仍然以r主导
# print(f.read())
# f.write('hello world')
# f = open('test2.txt', 'r+')  # 没有该文件会报错

# f = open('test2.txt', 'w+') # 重新创建覆盖了
# f.write('hello')
# print(f.read())  # 可读模式 但是指针写入时指向最后 读取为空
# print(f.readable())
















