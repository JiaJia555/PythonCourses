'''
四 isinstance和type的区别
'''
i = 1
s = 'jiajia'

print(isinstance(i, int))
print(isinstance(s, int))
print(isinstance(s, str))

print(type(i))

if isinstance(i, int):
# if type(i) == int:
    print(123)


class A:
    pass


class B(A):
    pass


b = B()
print(isinstance(b, B))  # True
print(isinstance(b, A))  # True 考虑类的继承关系

print(type(b) is B)  # True
print(type(b) is A)  # False 不考虑类的继承关系


# is 和 ==的区别： == value; is 内存地址
# x = y = [4, 5, 7]
# z = [4, 5, 7]
# x == y  True
# x == z  True
# x is y  True
# x is z  False
# id(x) = id(y) not equal id(z)

