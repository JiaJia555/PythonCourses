# def multi_table():
#     for i in range(1, 10):
#         for j in range(1, i+1):
#             print("{}*{}={}".format(j, i, (j*i)), end=' ')
#         print("")
#
# def multi_table1():
#     pass
#
#
# multi_table()
# multi_table1()
# # 一般写完函数再统一调用
# if __name__ == '__main__':
#     multi_table()
#     multi_table1()

# 传参
'''
实参是实在传入的参数
形参 接收的参数
'''

# def test(a):
#     a = 10
#     print('111', a)
#
#
# a =1            # 重新赋值
# test(a)
# print('222', a)
#
#
# def test1(li):
#     li.extend([4, 5])
#     print('111', li)
#
#
# li = [1, 2, 3]
# test1(li)
# print('222', li)


# 利用函数实现数字相加
# def sum_nums(num1, num2):
#     res = num1 + num2
#     print(num1)
#     print(num2)
#     print("{} = {} + {}".format(res, num1, num2))
#
#
# n1 = int(input("num1:"))
# n2 = int(input("num2:"))
# 位置参数 一一对应
# sum_nums(n2, n1)      # num1= n2
# 关键字餐厨 不受位置影响
# sum_nums(num2=n2, num1=n1)

# 有些参数必须传,也有一些是默认参数，不用传
# range(1, 10).index(value)
# def test2(a, b=2):
#     a = a+b
#     print(a, b)
#
#
# a = 1
# test2(a)

# import requests
# requests.get()          # et() missing 1 required positional argument: 'url'

# 动态参数 可变长度参数
# def test3(*args):
#     # *args-->默认返回元组
#     print(args)
#
#
# test3(1, 2, 3)

# def test3(*args):
#     # *args-->默认返回元组
#     print(args)
#
#
# # test3((1, 2, 3))            # ((1, 2, 3),)
# tu = [1, 2, 3]                # ([1, 2, 3],)
# test3(tu)

# def test4(**kwargs):
#     # 字典
#     print(kwargs)
#
#
# test4(a =1, b =2, c =3)         # {'a': 1, 'b': 2, 'c': 3}

# def test5(a, b, c):
#     # print(tu)                       # (1, 2, 3)
#     print(a, b, c)                    # 1 2 3
#
#
# tu = (1, 2, 3)
# test5(*tu)

# 元旦 36
# 元旦 春节 24
# 今天 春节

# def new_year():
#     dis_new_year = 36
#     print("距离元旦还有:{}".format(dis_new_year))
#     return dis_new_year
#
#
# def spring_fes(dis_new_year):
#     dis_spring_fes = dis_new_year +24
#     print("距离春节还有：{}".format(dis_spring_fes))
#
# # return 返回值 有返回 就要有接收
# new_years = new_year()
# spring_fes(new_years)


def test6():
    a = 1
    b = 2
    c = 3
    # return a        # return 之后就停止执行
    # return b
    # return c
    # return a, b, c          # 默认返回元组(1, 2, 3)
    return[a, b, c]             # [1, 2, 3]


# res = test6()
# print(res)
# 1, 2, 3
a, b, c = test6()
print(a, b, c)









