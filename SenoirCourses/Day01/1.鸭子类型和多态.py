# @ Time : 2019/12/25
'''
一 鸭子类型 （动态语言调用实例方法时不检查类型，
只要方法存在，参数正确，就可以调用）
'''
a = [1, 2]
b = [3, 4]
c = (5, 7)  # 元组
d = {7, 8}  # 集合 是无序的
# 1. append, extend的区别
# def extend(self, iterable): iterable: 可迭代的对象 可以用for
a.append(b)
print(a)  # 输出为[1, 2, [3, 4]]
a.extend(b)  # 输出为 [1, 2, 3, 4]
print(a)
a.extend(c)  # 输出为 [1, 2, 5, 7]
print(a)
a.extend(d)  # 输出为 [1, 2, 8, 7]
print(a)

# 二 多态


class Cat(object):
    def say(self):
        print('i am a Cat')


class Dog(object):
    def say(self):
        print('i am a Dog')

class Duck(object):
    def say(self):
        print('i am a Duck')


animal_list = [Cat, Dog, Duck]
for animal in animal_list:
    animal().say()








