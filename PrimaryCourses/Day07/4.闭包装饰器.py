def test():
    print('1111')

te = test() # te是函数的引用
print(id(test()))
print(id(te))
# 两个内存地址相同，指向相同

'''
外函数
内函数
闭包：
1. 在一个外函数中定义了一个内函数
2. 内函数里运用了外函数的临时变量
3. 并且外函数返回值是内函数的引用
一般情况下，当test()函数体执行完毕，则临时变量被释放
如果是闭包，那么外函数在执行过程中会感知内函数会有引用，
所以外函数将临时变量与内函数绑定，所以此时就可以引用外函数的临时变量
'''
# def test(number): # 临时变量
#     print("--1--")
#     def test_in(number_in):
#         print(number_in)
#         print("--2--")
#         return number_in + number
#     print("--3--")
#     return test_in      # 3
#
#
# res = test(20)            # res = test_in
# # print(res)              # 未调用内函数 <function test.<locals>.test_in at 0x00000094E072E9D8>
# print(res(25))            # 调用内函数

# def test(number):
#     print(number)
#     def test_in():
#         print(number)
#     test_in()
#
#
# test(20)