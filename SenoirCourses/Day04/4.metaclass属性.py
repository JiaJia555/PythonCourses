# 4. mentaclass 属性
# 如果一个类中定义了metalass = xxx,Python就会用元类的方式来创建类


def upper_attr(class_name, class_parents, class_attr):
    # print(class_name)        # Foo
    # print(class_parents)     # (<class 'object'>,)
    # print(class_attr)        # {'__module__': '__main__', '__qualname__': 'Foo', 'name': 'jiajia'}
    newattr = {}
    for name, value in class_attr.items():
        # print(name)         # __module__, __qualname__, name
        # print(value)          # __main__, Foo, jiajia
        if not name.startswith("_"):
            newattr[name.upper()] = value
    return type(class_name, class_parents, newattr)


class Foo(object, metaclass=upper_attr):   # metaclass 继承优先于object,会先去找upper_attr
    name = 'jiajia'


f = Foo()
print(f.NAME)
# print(f.name)   #  AttributeError: 'Foo' object has no attribute 'name'
print(hasattr(Foo, 'name'))  # False
print(hasattr(Foo, 'NAME'))  # True




















