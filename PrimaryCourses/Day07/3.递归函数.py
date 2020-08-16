# 4！ ---》 4*3*2*1

# i = 1
# result = 1
# while i <= 4:
#     result = result * i
#     i += 1
#
#
# print(result)

'''
递归函数
1. 调用自身函数
2. 递归可以做到的循环同样可以做到
3. 设置结束条件
4. 递归少用，效率很低
'''
# def nums(num):
#     if num > 1:
#         return num*nums(num-1)
#     else:
#         return 1
#
#
# res = nums(6)
# print(res)

# 内置方法
'''
filter 过滤
'''
# 实现返回1-10的奇数列表
# li = []
# for i in range(1, 11, 2):
#     # print(i)
#     li.append(i)
# print(li)

# li = []
# for i in range(1, 11):
#     if i%2 ==1:
#         li.append(i)
#
# print(li)

# 过滤器
# def is_odd(n):
#     return n % 2 ==1
#
#
# n = range(1, 10)
# print(list(filter(is_odd, n)))        # 返回迭代器，和map比较像

from functools import reduce
# reduce 函数对参数序列中元素进行累计
# def multi(x, y):
#     return x*y
#
# # muulti(1, 7)
# print(reduce(multi, range(1, 7)))           # [1,2,3,4,5,6]

# 匿名函数,无需重复调用，就使用匿名函数
# def f(x):
#     return x*x
#
# f(1)
# lambda关键字参数 返回值（表达式）
# f = lambda x, y: x * y
# print(f(5,6))

# def multi(x, y):
#     return x*y
from functools import reduce
print(reduce(lambda x, y: x*y, range(1, 7)))

'''
匿名函数可以直接作为返回值
'''


# def f(i, j):
#     return lambda: i +j
#
#
# res = f(6,6)            # 相等 res = lambda: i+j
# # print(res)              # <function f.<locals>.<lambda> at 0x000000F5FE55E708>
# print(res())                # 12

'''
匿名函数作为参数传递
'''
def test(a, b, func):
    res = func(a, b)        # res = lambda x, y: x+y
    return res


res = test(11, 22, lambda x, y: x+y)
print(res)

'''
高阶函数
1. 函数名可以作为参数传递
2. 函数名可以作为返回值
满足一个条件即可
'''
map()
zip()
filter()
reduce()










