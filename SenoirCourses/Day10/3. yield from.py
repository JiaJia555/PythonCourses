from itertools import chain

# lis = [1, 2, 3]
# dic = {
#     "name": "juran",
#     "age": 18
# }

# print(list(chain(lis, dic, range(5, 10))))
# [1, 2, 3, 'name', 'age', 5, 6, 7, 8, 9]

# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         # for value in my_iterable:
#         #     yield value
#         yield from my_iterable        #相当于for 循环
#
#
# for value in my_chain(lis, dic, range(5, 10)):
#     print(value)
#     # pass

# 多个可迭代对象直接输出结果
# for value in chain(lis, dic, range(2, 8)):
#     print(value)

# def generator_1(lis):
#     yield lis
#
#
# def generator_2(lis):
#     yield from lis
#
#
# for i in generator_1(lis):
#     print(i)    # [1, 2, 3]
#
#
# for i in generator_2(lis):
#     print(i)    # 1, 2, 3

# yield from demo


def generator_1():          # 子生成器
    total = 0
    while True:
        x = yield
        print('加', x)
        if not x:           # if not None: True
            break
        total += x
    return total


def generator_2():  # 委托生成器
    while True:
        # 建立调用方和子生成器的通道
        total = yield from generator_1()  # 子生成器
        print('加和总数是:', total)


def main():  # 调用方
    # g1 = generator_1()
    # g1.send(None)
    # g1.send(2)
    # g1.send(3)
    # g1.send(None)
    g2 = generator_2()
    g2.send(None)
    g2.send(2)
    g2.send(3)
    g2.send(None)


if __name__ == '__main__':
    main()