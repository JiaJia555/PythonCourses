class A:
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')
        # python 2
        # super(B, self).__init__()
        super().__init__()


# 1. 重写了B的构造函数 为什么还要去调用super
# 数据冗余
# b = B()

class People(object):
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight

    def speak(self):
        print("s% 说: 我%d岁了"%(self.name, self.age))


class Student(People):
    def __init__(self, name, age, weight, grade):
        # self.name = name
        # self.age = age
        # self.weight = weight
        # super().__init__(name, age, weight)
        People.__init__(self, name, age, weight)
        self.grade = grade

    def speak(self):
        print("%s 说:我%d岁了 我在读%d年级"% (self.name, self.age, self.grade))


s = Student('lg', 10, 30, 3)
s.speak()

# super 执行顺序到底是什么样的


class A:
    def __init__(self):
        print("A")


class B(A):
    def __init__(self):
        print("B")
        super().__init__()


class C(A):
    def __init__(self):
        print("C")
        super().__init__()


class E:
    pass


class D(B, C, E):
    def __init__(self):
        print("D")
        super().__init__()


d = D()
print(D.__mro__)  # D B C A
# super不是之前讲的调用父类中的方法
# 而是按照 mro 算法来调用的




