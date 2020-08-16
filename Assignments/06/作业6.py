# 1. lis1 = ["name", "author", "introduce"]
# lis2 = ["NORWEIGN WOOD", "Haruki Murakami", "balalalalal..."]。
# 将lis1 与lis2 以键值对的形式呈现
lis1 = ["name", "author", "introduce"]
lis2 = ["NORWEIGN WOOD", "Haruki Murakami", "balalalalal..."]
print(dict(zip(lis1, lis2)))

'''
2 生成了N个1-1000之间的随机整数(N<=1000)
N 是用户输入的，对于其中重复的数字，只保留一个，去掉其余相同的，
然后把这些数字从小到大排列。（注意：此处需要使用随机整数。可了解random
模块具体方法，for循环，range()函数等结合使用）
'''
import random
a_lis = []
for i in range(1, 1000):
    num = random.randint(1, 1000)
    a_lis.append(num)

print(a_lis)
print(len(a_lis))
b = list(set(a_lis))
print(b)
print(len(b))
b.sort()
print(b)

'''
3.基于上一题，将已经去重的数据做一个判断，如果大于500的则添加到一个
列表中，否则放到另一个列表
'''
c = []
d = []
for i in b:
    if i > 500:
        c.append(i)
    else:
        d.append(i)

print(c)
# print(d)

'''
4. 有如下值li=[11, 22, 33, 44, 55, 77, 88, 99, 90]
将所有大于等于66的值保存至字典的第一个key中， 将小于66的值
保存至第二个key的值中
'''
li=[11, 22, 33, 44, 55, 77, 88, 99, 90]
dic={}
list_1 = []             # 大于等于66
list_2 = []             # 小于66

for i in li:
    if i >= 66:
        list_1.append(i)
    else:
        list_2.append(i)
print(list_1)
print(list_2)
dic.setdefault('k1', list_1)
dic.setdefault('k2', list_2)
print(dic)