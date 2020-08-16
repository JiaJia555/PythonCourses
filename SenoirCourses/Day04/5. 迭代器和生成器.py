# 5.1 迭代器
# 迭代：通过for循环遍历对象的每一个元素的过程。
# 迭代器是一种可以被遍历的对象，并且能作用于next()函数。迭代器对象从集合的第一个元素开始访问，
# 直到所有的元素被访问完结束。迭代器只能往后遍历不能回溯，不像列表，你随时可以取后面的数据，也可以返回头取前面的数据。
from collections.abc import Iterator, Iterable
print(isinstance(list(), Iterable))   # True iter方法
print(isinstance(list(), Iterator))   # False  next方法

# iter next
l = [1, 2, 3, 4]
it = iter(l)
print(it)               # <list_iterator object at 0x0000003316E876C8>
print(next(it))         # 1
print(next(it))         # 2
print(next(it))         # 3
print(next(it), '_')    # 4_

# for i in it:
#     print(i)


# 5.2 生成器
# 10**20
g = (x for x in range(10))   # 列表推导式换成()
j = [x for x in range(10)]   # 列表推导式
print(g)                     # <generator object <genexpr> at 0x00000060AF8487C8>
print(j)                     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# 生成器和迭代器类似，都是通过next取值
print(next(g))
print(next(g))
print(next(g))
print(next(g))
print(next(g))
# 或者用for 循环
for i in g:
    print(i)

# 斐波那契数列, a, b = b, a + b


def fibonacci():
    print("--func start--")
    a, b = 0, 1
    for i in range(5):
        # print(b)
        print("--1--")
        yield b
        print('--2--')
        a, b = b, a + b
        print('--3--')
    print("--func end--")


g = fibonacci()
print(next(g))  # --func start--, --1--, 1
print(next(g))  # --2--, --3--, --1--, 1
print(next(g))
print(next(g))


# 实例分析，生成器如何读取大文件
def readlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            # index 2
            pos = buf.index(newline)
            # print(pos)    #遇到{|}停下来
            yield buf[:pos]
            buf = buf[pos + len(newline):]

        chunk = f.read(4096*10)
        # 读到文件末尾
        if not chunk:
            yield buf
            break
        buf += chunk


with open('demo.txt') as f:
    for line in readlines(f, "{|}"):
        print(line)


