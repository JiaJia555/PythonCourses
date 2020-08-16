'''私有属性类的内部可以访问和调整改变，外部不可以，一般定义__双横线
_init_默认返回None, _str_默认返回1
'''

'''
不希望外部去访问我的一个属性
私有属性--> __属性名
类的内部是可以访问私有属性
静态方法不传self
'''
class People(object):
    def __init__(self):
        self.__age = 18 # 私有属性 类的外部访问不到
        self.name = "amy"

    # MD5+salt
    def get_age(self):
        print(self.__age)

    def set_age(self,age):
        self.__age = age


amy = People()  # amy-->self
print(amy.name)
# print(amy.__age)
amy.get_age()
amy.set_age(22)
amy.get_age()
print(amy.__dir__())    # 查看对象的方法跟属性

print("-"*20)
print(amy.__dir__())

class Demo(object):
    def __init__(self):
        self.name = "amy"   # 实例属性

    def __str__(self):
        # self.name = "xiaoyong"
        return 1111

    # 实例方法
    def test(self):
        self.name = "amy"
        print(self.name)
    #
    # def test1(self):
    #     print(self.name)


d = Demo()
# d.test()
# print(d.name)
# print(d)
# print(d.__str__())

'''
私有方法
'''
class Demo(object):
    def test1(self):
        print("test1")

    def __test2(self):
        print("test2")

d = Demo()
d.test1()
d.__test2()

'''
成员 属性:类属性(静态属性) 实例属性
'''
# class Province(object):
#     country = "中国"  # 类属性 静态属性 对象（self) 类来调用
#
#     def __init__(self,name):
#         self.name = name
#         # self.country = "中国" # 实例属性 对象/每一个对象都有的内容，占用内存/也是动态属性
#
#     def print_info(self):
#         # print(self.country,self.name)
#         print(Province.country,self.name) #self也可调用
#
#
# guangdong = Province("广东")
# chongqing = Province("重庆")
# guangdong.print_info()
# chongqing.print_info()

'''
实例方法:对象需要保存的一些值 执行某功能时 需要使用对象中的值
静态方法:跟我们在函数外部定义独立的方法没有什么区别,但是有的是方便维护。不需要创建对象 直接访问 不需要self参数 。调用 通过类调用

类方法:保存在类中 由类直接调用 cls-->当前类
'''
class Demo(object):
    def __init__(self):
        self.name = "amy"

    def test(self):
        print(self.name)

    @staticmethod   # 静态方法
    def test1(name):
        print(name)

    @classmethod
    def class_md(cls):
        print(cls)

d = Demo()
d.test()
Demo.test1("吴先生")
d.test1("小周")

Demo.class_md()  #可以直接d.class_md()???

'''
在类当中 去写一个 输出当前格式化时间方法
'''
# import time
#
# class TimeTest:
#     @staticmethod
#     def show_time():
#         print(time.strftime("%H:%M:%S",time.localtime()))
#
#
# nowtime = TimeTest()
# TimeTest.show_time()


# def show_time():
#     print(time.strftime("%H:%M:%S", time.localtime()))
#
# show_time()

'''
属性(实例属性,类属性)
三种方法(实例方法,静态方法,类方法)
'''
# class Demo:
#     def __init__(self):
#         self.name = "amy"
#
#     @property   # 将方法变为属性
#     def test(self):
#         print(self.name)
#         return "test"
#
#     @test.setter    # d.test = "456"
#     def test(self,nums):
#         print(nums)
#
#     @test.deleter
#     def test(self):
#         print(1111)
#
# '''调用方法和调用属性/有无小括号'''
# d = Demo()
# print(d.name)
# d.test() #调用方法
# res = d.test #调用属性
# print(res)
#
# d.test = "456"  # 想要改变
#
# del d.test



'''
django 
'''
# class Demo1:
#     def test1(self):
#         return 111
#
#     def test2(self):
#         print(123)
#
#     def test3(self):
#         print("del")
#
#     per = property(fget=test1,fset=test2,fdel=test3)
#
#
# d1 = Demo1()
# res = d1.per
# print(res)

'''
翻页
1 0-10  0-9 10条
2 10-20 10-19 10条
3 20-30
'''
class Page:
    def __init__(self,current_page):
        try:
            p = int(current_page)
        except Exception as e:
            p = 1
        self.page = p

    @property
    def start(self):
        start = (self.page-1)*10
        return start

    @property
    def end(self):
        end = self.page * 10
        return end


li = list(range(100))
# print(li)
while True:
    p = int(input("请输入要查看的页码:"))
    page = Page(p)
    # start = (p - 1) * 10
    # end = p * 10
    # print(li[start:end])
    # print(li[page.start():page.end()])
    print(li[page.start:page.end])

