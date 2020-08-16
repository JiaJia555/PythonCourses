'''
2. Python的列表是一个有序可重复的元素集合，
可嵌套、迭代、修改、分片、追加、删除，成员判断。
从数据结构角度看，Python的列表是一个可变长度的顺序存储结构，
每一个位置存放的都是对象的指针。

列表是可变类型
'''
a = list()
print(a)
b = list('hello')       # 括号内是可迭代对象
# ['h', 'e', 'l', 'l', 'o']
print(b)
b[0] = 1
print(b)
del b[2]
print(b)
print(id(b))
b.remove('o')
print(b)
print(id(b))

c = [1, 2, 3, 4, 5, 6]
c.pop()     # 默认删除最后一个
print(c)

del c   # 删除列表
# print(c)    # c is not defined

# 1.列表的组合
li1= [1, 2, 3]
li2= [4, 5, 6]
print(li1 + li2)

# 2.列表的乘法
print(li1*2)        # 重复2次
# 3.判断元素是否在列表内部
# in
# 4.迭代列表中的每个元素
for i in li2:
    print(i)

'''
len(list) 返回列表元素个数，也就是获取列表长度
max(list) 返回列表元素最大值
min(list) 返回列表元素最小值,整型和字符串比较会报错
list(seq) 将序列转换为列表
'''
li4 = list('123456')
print(li4[::-1])
d = li4.reverse()      # 改变原有的li4，之前的都不会改变,返回为None
print(li4)
li4.sort(reverse=False)           # 默认，升序
print(li4)

li5 = [1, 2, 3, ['amy', 1]]
print(li5[3][0])

li6 = [1, 2, 3]
# append(obj)
# [1, 2, 3, [2, 3]]
li6.append([2, 3])
print(li6)
# count(obj)
print(li6.count(3))         # 1
# extend(seq)
li6.extend([4, 5])
print(li6)          # [1, 2, 3, [2, 3], 4, 5]
# index()
print(li6.index(2))     # 1
# insert(index, obj)
li6.insert(2, 'logic')
print(li6)          # 前面插入 [1, 2, 'logic', 3, [2, 3], 4, 5]
# pop(obj=list[-1])
li6.pop()
print(li6)          # [1, 2, 'logic', 3, [2, 3], 4]
# remove(obj)
li6.remove(3)
print(li6)          # [1, 2, 'logic', [2, 3], 4]
# reverse()
li6.reverse()
print(li6)          # [4, [2, 3], 'logic', 2, 1]
print('------')
# sort([func])
# li6.sort()
# print(li6)          # 报错，列表和整型和字符串不能比较大小
# copy()        # 拷贝
# li7 = li6.copy()
# print(li7)
# clear()
# li7.clear()
# print(li7)            # []
# del是删除列表，clear是清空列表的元素
