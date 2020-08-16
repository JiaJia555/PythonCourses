# 5.经典的参数错误
def add(a, b):
    a += b
    # a = a + b
    return a


a = 1
b = 2
c = add(a, b)
print(c)     # 3
print(a, b)  # 1 2

a = [1, 2]
b = [3, 4]

c = add(a, b)
print(c)      # [1, 2, 3, 4]
print(a, b)   # a = [1, 2, 3, 4], b = [3, 4]

a = (1, 2)
b = (3, 4)

c = add(a, b)
print(c)      # (1, 2, 3, 4)
print(a, b)   # a = (1, 2), b = (3, 4)
# 总结
# 数字和元组都是不可变类型，所以a=a+b相当于重新创建了一个c, a,b的值都没有变
# 列表是可变类型（内存地址不变），a=a+b相当于改变了a并赋值给c,所以a变了（a的内存地址不变）

#小整数对象池： -5 -256
a = 1
b = 1
print(a is b)  # true

a = 2222
b = 2222
print(a is b)  # Pycharm 输出为true, 交互环境下应该输出False