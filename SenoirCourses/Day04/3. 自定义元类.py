# 3.自定义元类
# 3.1 动态创建类


def create_class(name):
    if name == 'user':
        class User(object):
            def __str__(self):
                return "user"
        return User
    elif name == 'student':
        class Student:
            def __str__(self):
                return "student"
        return Student


if __name__ == '__main__':
    myclass = create_class('user')
    obj = myclass()
    print(obj)                # user
    print(type(obj))          # <class '__main__.create_class.<locals>.User'>

# 3.2 使用type创建类
# type源码有两种功能
# type(object) -> the object's type        查看数据类型
# type(name, bases, dict) -> a new type    创建新类, type(类名,由父类组成的元组,包含属性的字典)

Greeks = type("Greeks", (), {})
alpha = Greeks()
print(alpha)     # <__main__.Greeks object at 0x0000009F452DE5C8>

# type 和正常创建类的结果是一样的
class Fruits:
    pass
apple = Fruits()
print(apple)      # <__main__.Fruits object at 0x000000B8EFCCE848>

# 3.2.1 添加属性
User = type("User", (), {'name': "jiajia"})
obj = User()
print(obj)
print(obj.name)   # jiajia

# 3.2.2 添加方法
def demo(self):
    return self.name


def get_age(self):
    self.age = 18
    return self.age


#  添加魔法方法, 不适用
def __init__(self):
    self.sex = 1


User = type("User", (), {'name': "jiajia", 'info': demo, "age": get_age, "sex": __init__})
obj = User()
print(obj.info())   # jiajia
print(obj.age())    # 18
print(obj.sex())    # None, 魔法方法没有返回


# 3.2.3 继承父类,可继承多个类
class BaseClass(object):
    def test(self):
        return 'base class'

class BaseClass1(object):
    def test1(self):
        return 'base class1'


User = type("User", (BaseClass, BaseClass1,), {'name': "jiajia"})
user = User()
print(user.test())    # base class
print(user.test1())   # base class1

# 魔法方法可继承吗？
# 可以
class B1(object):
    def __str__(self):
        return '魔法方法可继承'

class C1(B1):
    pass

x = C1()
print(x)  # 魔法方法可继承