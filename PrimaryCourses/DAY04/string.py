'''
3-字符串是不可变的序列数据类型，不能直接修改字符串本身，
和数字类型一样
'''
# 换行
s1 = 'hello \\n oldamy'
print(s1)

s2 = "hello oldamy"
print(s2)

# 保留字符串原有格式
s3 = '''hello 
oldamy'''
print(s3)

name = "hello oldamy"
print(name[1])      # 第二位
print(name[-1])     # 最后一位

# name[4] = 'l'       # 'str' object does not support item assignment

print(len(name))
print(name[6:12])       # 左闭右开
print(name[6:])
print(name[-7:])        # oldamy
print(name[:])          # hello oldamy

print(name[::2])        # hloodm
print(name[::-1])       # ymadlo olleh

'''
1.索引默认从0开始
2.切片时左闭右开
3.当是取单个字符的时候,索引超出范围会报错。而切片时不会报错。
4.步长不能为0，也不允许为浮点数
5.int必须是十进制
'''
name = 'amy'
age = 18
print('%s年龄%d'%(name, age))
print('{1}年龄{0}'.format(age, name))

# s4 = "hello python"
# print(s4.find('e'))     # 1
# print(s4.find('o'))     # 4 返回最小的值
# print(s4.find('0'))     # 未找到返回-1
# print(s4.rfind('o'))    # 10 返回最大值
# print("-"*20)
# print(s4.index('w'))    # 找不到index报错

s5 = "hello oldoldamy"      # 全部替换
print(s5.replace('old', 'beautiful', 1))        # 本身没有被替换

s6 = "hello everybody ye"
print(s6.split('e'))        # 返回列表
# startswith判断以什么开始
print(s6.startswith('h'))       # 返回布尔值
print(s6.endswith('ye!'))

s7 = 'JIAJIA jiajia'
print(s7.lower())
print(s7.upper())

s8 = '   jiajia  '
print(s8.strip())
print(s8.lstrip())
print(s8.rstrip())

