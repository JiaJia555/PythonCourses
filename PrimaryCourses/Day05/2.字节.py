# 字节
a = b"hello"
print(a)
print(type(a))
# b = bytes('hello')            # 报错
b = bytes('hello', encoding='utf8')
print(b)

print(str(a))           # b'hello'
print(a.decode())
print(a)                # b'hello'

c ='hello'
print(c.encode())
'''
bytes数据类型在所有的操作和使用甚至内置
方法上和字符串数据类型基本一样，也是不可变的
序列对象。
'''