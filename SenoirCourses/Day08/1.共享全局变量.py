import threading


num = 0


def demo1(nums):
    global num
    for i in range(nums):
        num += 1
    print('demo1---num:%d' % num)


def demo2(nums):
    global num
    for i in range(nums):
        num += 1
    print('demo2---num:%d' % num)


def main():
    t1 = threading.Thread(target=demo1, args=(100000,))
    t2 = threading.Thread(target=demo2, args=(100000,))

    t1.start()
    t2.start()

    print("main---num:%d" % num)


if __name__ == '__main__':
    main()

# 循环100次输出结果为
'''
demo1---num:100
demo2---num:200main---num:200
'''

# 循环100000次输出结果如下，发现了输出结果和期望值100000/200000并不相同
# 原因： cpu运行原理，时间片轮转
'''
main---num:143131demo1---num:100000
demo2---num:195747
'''