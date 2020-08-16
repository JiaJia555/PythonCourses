'''面向过程'''
# def stu_info(name,age,gender):
#     print(name,age,gender)
#
# stu_info("oldli","18","male")
# stu_info("ellen","18","male")
# stu_info("bruin","18","male")

'''面向对象'''
# class Students(object):
#     def stu_info(self,name, age, gender):
#         print(name, age, gender)
#
# s = Students()
# s.stu_info("oldli","18","male")
# s.stu_info("ellen","18","male")
# s.stu_info("bruin","18","male")

'''
self 形参
self 是对象本身 也就是说 当创建的对象是谁时 self就是谁
'''
# class Student(object):
#     def test(self):
#         # print(self)
#         pass
#
# oldli = Student()
# print(oldli)
# oldli.test()
#
# Chy = Student()
# print(Chy)
# Chy.test()

# li = [1,2,3,4]
# li = list(li) #list 也是一个类，li是实例化一个对象
# li.append()

# class Student(object):
#     def info(self):
#         print(self.name,self.age)
#
# marshal = Student()
# marshal.name = "marshal"
# marshal.age = "18"
# # print(marshal) #输出内存地址
# marshal.info()
#
# xiaoming = Student()
# xiaoming.name = "xiaoming"
# xiaoming.age = "22"
# # print(marshal)
# xiaoming.info()


# class Students(object):
#     def stu_info(self,name):
#         print(name, self.age, self.gender)
#
# s = Students()
# s.age = "18"
# s.gender = "male"
# s.stu_info("oldli")
# s.stu_info("ellen")
# s.stu_info("bruin")

'''
构造方法(初始化方法)
def __init__(self):
    pass
特殊意义
    创建对象的同时 通过对象执行这样的一个方法 叫做构造方法
'''
# class Student(object):
#     def __init__(self):
#         print("---1---")
#
# bruin = Student()   # 输出---1---，因为两行代码是同时运行的__init__(self)
# print(bruin)

# class Students(object):
#     def __init__(self,age,gender):
#         # 属性
#         self.age = age
#         self.gender = gender
#         self.addr = "ChangSha"
#
#     # 打印信息的行为
#     def stu_info(self,name):
#         print(name, self.age, self.gender,self.addr)
#
#
# s = Students("18","male")
# # s.age = "18"
# # s.gender = "male"
# s.stu_info("oldli")
# s.stu_info("ellen")
# s.stu_info("bruin")

'''
def __str__(self):
    pass
1.return关键字 将我们的信息直接返回 对象
2.只能是str 如果非字符串 str()
'''
# class People(object):
#     def __init__(self):
#         self.age = 18
#         self.name = "amy"
#         self.hobby = "reading"
#
#     def __str__(self):
#         info = "{}的年龄{},他的爱好{}".format(self.name,self.age,self.hobby)
#         # return str(self.age),self.name,self.hobby
#         # return 返回的多个值 元组
#         # 一定返回字符串
#         return str({"name":self.name,"age":self.age})
#
#
# amy = People()  # amy = str(self.age)
# print(amy)
# str()

'''
只有当年龄>0的时候才返回出来
否则默认为0岁
'''
# class People(object):
#     def __init__(self):
#         self.age = 0
#
#     def set_age(self,new_age):
#         if new_age >= 0 and new_age <= 120:
#             self.age = new_age
#         elif new_age > 120:
#             self.age = 0
#         else:
#             # abs()取绝对值的内置方法
#             self.age = abs(new_age)
#
#     def get_age(self):
#         return self.age
#
# xiaoming = People()
# xiaoming.set_age(10)
# print(xiaoming.get_age())

'''
1.函数只有在被调用的时候才会执行
2.for执行完毕之后 i=9
'''
# res = [lambda x:x+i for i in range(10)]
# print(res)
# print(res[9](10))

'''
i随着for 循环变动
'''
# res1 = [lambda x,i=i:x+i for i in range(10)]
# print(res1[2](10))


