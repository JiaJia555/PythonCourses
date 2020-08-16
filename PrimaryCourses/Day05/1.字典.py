'''
Python的字典数据类型是基于hash散列算法实现的，
采用键值对(key:value)的形式，根据key的值计
算value的地址
'''
jiajia = {"age": '18', "addr": "macau"}
# 字典访问
print(jiajia["addr"])
# jiajia = {"age": '18', ["addr"]: "macau"} 会报错，因为key值不可是可变类型
# 如果key值重复,以最后一个为主
jiajia = {"age": '18', "addr": "macau", "addr":"HK"}
print(jiajia)

# 空字典
a = dict()
print(a)

# 创建列表
amy = dict(age=18, addr='hunan')
print(amy)
ami = dict([("age", 'addr'), (18, 'hunan')])
print(ami)              # {'age': 'addr', 18: 'hunan'}
# map创建
a = [1, 2, 3]
b = [4, 5, 6]
# [(1,4), (2, 5), (3, 6)]
print(map(str, a))          # 返回对象
# 列表中的每个元素都转换成字符串
print(list(map(str, a)))       #强转列表
# ['1', '2', '3', '4']


def fmap(a,b):
    return(a,b)


print(dict(map(fmap, a, b)))
print(dict(zip(a, b)))          # 打包

# 添加新元素
jiajia['sex'] = 'female'
print(jiajia)
# {'age': '18', 'addr': 'HK', 'sex': 'female'}
jiajia['sex'] = 'male'
print((jiajia))

# dict 没有remove
# pop
jiajia.pop("addr")
print(jiajia)

# del
# del jiajia
# print(jiajia)  # 字典不存在

# jiajia.clear()
# print(jiajia)       # 空列表

dic1 = {'name': 'jiajia', 'height': "1.6"}
print(dic1.get('name'))
print(dic1.get('weight'))       # None,没有报错

# print(dicl['weight'])
# print(dic1['name'])
# print(dic1.items())
for key, value in dic1.items():
    print(key, value)

# 只取key值
print(dic1.keys())
print(dic1.values())

dic2 = {"wu": 90, "li": 88, "zang": 84}
# print(sorted(dic2))           # ['li', 'wu', 'zhang']
# 用成绩排名
# x = ['wu', 'li', 'zhang']
# y = [90, 88, 84]
# print(sorted(list(zip(x, y))))
# [('li', 88), ('wu', 90), ('zhang', 84)]
print(sorted(list(zip(dic2.values(), dic2.keys()))))
# [(84, 'zang'), (88, 'li'), (90, 'wu')]







