a = {}
print(type(a))          # <class 'dict'>

# 定义空集合
d = set()
print(type(d))          # <class 'set'>
s = (1, 2, 3, 4, 5)
s1 = set('1234')
print(s1)
# 自动去重,无序的
s2 = set("hello jiajia")
print(s2)

# 添加元素
s1.add('3')
print(s1)

s1.add('6')
print(s1)
# 添加字符串
s1.add('jiajia')
print(s1)
# 添加列表,字典（可变） 会报错
# s1.add([1, 2, 3])
# print(s1)

# append/extend
# update
s1.update('hello')
print(s1)
# {'2', '6', 'e', 'jiajia', 'l', '4', 'o', '3', 'h', '1'}

# 删除
s1.remove('3')
print(s1)
# pop方法,随机删除一个元素，无序，不能靠索引删除
s1.pop()
print(s1)

# 可变类型不会改变id
print(__name__)                 # main