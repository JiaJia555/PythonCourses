'''
3.1 运算符
做除法返回的是浮点数,并且都是向下取整

//为整除,所以返回的是整数部分,并不是整数类型。当除数与被除数有为浮点数
的时候 返回的是整数部分的浮点数

取余也是先遵循向下取整的规则,divmod(x//y, x%y)-->divmod(商,余数)
'''
# 1.算术元运算符
print(10/3)     # 3.3333333333333335
a = divmod(10, 3)       # Return the tuple (x//y, x%y)
print(a)

b = 0.1 + 0.1 + 0.1 - 0.3
print(b)                 # 5.551115123125783e-17  二进制

# 保留十进制
from decimal import Decimal
c = Decimal("0.1") + Decimal("0.1") + Decimal("0.1") - Decimal("0.3")
print(c)
# 2.比较运算符
'''
== 判断相等
!= 判断不等
'''
# str与Int不能直接比较
# 字符串与字符串的比较是转为ascii比较
# 'abc' < 'xyz'         # True
# (3, 2) < (‘a’, ‘b’)   # 报错，不能比较'<' not supported between instances of 'int' and 'str'
# True == 1             # True
# False == 0            # True
# (3>2)>1               # False
# (3>2)>2               # False

# 3 赋值运算符
'''
+=
-=
/=
'''
# 4 逻辑运算符
'''
x = 10
y = 20
x and y, 找错的，如果x为False,则输出False, 否则输出y的值
x or y, 找对的，x 是 True，它返回 x 的值，否则它返回 y 的计算值
not, 如果 x 为 True，返回 False 。如果 x 为 False，它返回 True。
'''
# 5 位运算符
'''
&
|
'''
# 6 成员运算符
'''
in 
not in
'''
# 7 身份运算符
'''
is 
is not
is 和 == 的区别
'''
name = ['吱呀', 'Jimmy', 'AT', 'jiajia']
if 'AT' in name:
    print('True')

# 8 三目运算
a = 2
b = 1
if a > b:
    print(a-b)
else:
    print(a+b)
print(a-b if a > b else a-b)
'''
3.2 数据类型
数据类型：整形int, 浮点型float, 复数类型complex, 布尔类型bool
容器类型: str,list, tuple, set, dictionary.
'''
# 数字类型是不可变类型
'''
通常用十进制表示数字，但有时我们还会用八进制或十六进制来表示：
十六进制用0x前缀和0-9，a-f表示，例如：0xff00
八进制用0o前缀和0-7表示，例如0o45
'''
# 整数缓存区
a = 10000
print(id(a))

del a

b = 10000
print(id(b))

int()
weight = 44.7
print(type(weight))
print(int(weight))

# 源码int(x, base=10) 转成整数
print(int('0b100', base=0))   # 4
print(bin(4))

height = 160
print(float(height))  # 转成浮点类型

import math  # 导入模块
print(math.ceil(4.1))      # 5
print(math.floor(4.5))     # 4
print(math.pow(2, 3))      # 8

# 四舍五入，四舍六入五双非
# 内置方法
round()
round(4.5)    # 4
round(3.5)    # 4

# 绝对值
print(abs(-1))

# 布尔类型
if True:
    pass
else:
    pass

while True:
    pass

# bool() 布尔类型
bool(0)      # False
bool(1)      # True
bool(2)      # True
bool('abc')  # True
bool("")     # False 空字符串为false，其他为错
bool(0.0)    # False
bool(0.1)    # True
bool(True)   # True
# None 永远是false,数据类型是Nonetype
'''
整数和浮点数，0表示False，其他为True
字符串和类字符串类型（包括bytes和unicode），空字符串表示False，其他为True
None永远表示False
'''


