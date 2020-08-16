# 1. __getattr__魔法方法
# 1.1 什么时候用__getattr__?当属性查找不到的时候用
from datetime import date


class User:
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        # print(self.birthday)
        self.info = info

    # 在查找不到属性的时候调用
    def __getattr__(self, item):
        # print(item, "attribute not found")
        # print(item)    # age
        # return "attribute not found"        # 不想输出None,可以将函数改成return
        return self.info[item]                # 用字典的键取值
        # return self.info.get(item)          # dict.get(key, default=None)
    # __getattribute__在__getattr__之前执行

    # def __getattribute__(self, item):
        # return "jia+"


if __name__ =="__main__":
    # 1996-12-10
    user = User('jiajia', date(year=1996, month=12, day=10), info={'age': 18})
    print(user.name)
    # 用__getattr__之前，AttributeError: 'User' object has no attribute 'age'
    print(user.age)        # 打印一个没有返回值的函数，默认输出None
    # print(user.gender)   # KeyError: 'gender'

# 1.2 info{}添加新属性
# print(user.age)返回18
# 这个时候输入新的属性还是会报错，字典的报错KeyError: 'gender'
# 如果不想要报错，return self.info.get(item) 返回None

# 1.3 __getattribute__魔法函数
# 先执行这个函数返回 jia+