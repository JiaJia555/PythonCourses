# 1.玩个特别无聊的游戏,猜数字。
# 玩家输入一个数字与
# 计算机随机生成的数字作对比
# 当两个值相等时,则说明用户猜对了
# 注意:外部不能获取到计算机随机生成的值
import random
# 思路
# player = int(input("请玩家输入1-10数字:"))
# var = random.randint(1,10)
# if player == var:
#     print("猜对了")
# else:
#     print("猜错了")
# 答案
# class Number(object):
#     def __init__(self):
#         self.__var = random.randint(0, 10)
#     def get_var(self):
#         print(self.__var)
# x = Number()
# #x.get_var()
# while True:
#     player = int(input("请玩家输入0-9数字:"))
#     if player == x:
#         print("猜对了")
#     else:
#         print("猜错了")


# 2. 《寻欢作乐》《面纱》《月亮与六便士》《刀锋》...这些书籍的作
# 者都是毛姆,并且管理员想统计每本书籍阅读的时长。使用面向对象
# 的方式输出毛姆:《书籍名》总共阅读:**小时
# import time
# class BookManage(object):
#     book_author = "毛姆"
#
#     def __init__(self, book_name):
#         self.book_name = book_name
#         self.nums = 0
#
#     def reading_time(self, reading_hours): #和煎饼比较像
#         self.nums += reading_hours
#         #print (self.nums)
#
#     def print_info(self):
#         print("{}:{}总共阅读{}小时".format(
#             BookManage.book_author, self.book_name, self.nums
#         ))
#
#     @staticmethod
#     def get_nowtime():
#          print(time.strftime("%H:%M:%S", time.localtime()))
#
#     @classmethod
#     def set_author(cls):
#         cls.book_author ="王小波"
#         print(cls.book_author)
#
# book1 = BookManage ("《寻欢作乐》")
# book2 = BookManage("《月亮与六便士》")
# book1.reading_time(2)
# book1.reading_time(2)
# book1.print_info()
# book1.get_nowtime()
# book1.set_author()


# 3. 在第二题的内部,打印输出本地时间(注意,并不使用到对象的属性
# 及方法)
# 4. 类中有一个私有属性,__age。想要在外部可以对其访问,改变,删除
# ,使用property 的fget,fset,fdel。
class friends(object):
    def __init__(self):
        self.__age = 16

    def test1(self):
         print(self.__age)

    def test2(self, nums):
         print(nums)

    def test3(self):
         print("del")
    per = property(fget=test1, fset=test2, fdel=test3)

f1 = friends()
res = f1.per
print(res) #函数没有返回值，所以是none
f1.per = "666"
del f1.per  # why

# 5.面向对象成员分为属性与行为，那属性与行为又分为哪些?
'''
属性有实例属性和类属性, 类属性又叫静态属性，实例属性包含私有属性
行为有三种方法(实例方法（包含私有方法）,静态方法,类方法)
'''
# 6.@staticmethod,@classmethod,@property 分别实现什么样的作用?
'''
使用staticmethod装饰器时，在类中定义函数时，括号中无需传递self参数，且在使用时也无需实例化类，可直接类名调用方法。

使用classmethod装饰器时，在类中定义函数时，括号中无需传递self参数，但是要传递cls的参数，这个参数为类，但是在使用时也无需实例化类，也可以直接调用函数使用。

使用property装饰器时，在使用时可发现不需要在方法后面加入括号，可以直接当作为一个类的属性来使用。
'''