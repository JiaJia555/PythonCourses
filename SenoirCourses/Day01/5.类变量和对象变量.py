'''
五 类变量和对象变量
'''
class A:
    # 类属性
    aa = 1
    # 实例方法
    def __init__(self, x, y):
        # 实例属性
        self.x = x
        self.y = y
        # self.aa = 22

a = A(1, 2)
print(a.x, a.y, a.aa)  # 输出， 可以向上查找

# print(A.x)   # 报错 不可以向下查找
print(A(1, 2).x)  # 输出 1
A.aa = 11  # 重写类属性
a.aa = 22  # self.aa =22
print(a.aa)  # 22
print(A.aa)  # 11

b = A(1, 2)
print(b.aa)  # 11

