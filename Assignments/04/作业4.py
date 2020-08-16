# 3. 怎么使'1'+2的结果输出为3？
print(int('1') + 2)

# 4. 'a'>1 True还是False?Why?
# 字符串与字符串比较才会转为阿斯克码
# if 'a' > 1:
#     print('T')
# else:
#     print("F")
'''
TypeError: '>' not supported between instances of 'str' and 'int'
'''
# 5.
s = "Have a nice weekend everyone"
# 取出a
print(s[5:6])
# print(s[len(s)])    # 输出的是那个元素?
# print(s[len(s)])  # 报错  out of range
# 截取出nice
print(s[7:11])
# 截取nice weekend
print(s[7:19])
# 取出整个s 两种方式(切片与一个方法)
print(s[0:28])
print(s)
# print(s[0:21])  # 输出的是哪一段?
print(s[0:21])    # Have a nice weekend e
# 将字符串隔一个字符取一个
print(s[::2])
# 将s逆序输出 多种方式(切片与方法)
r = s[::-1]
print(r)

# 使用reduce()
from functools import reduce
t = reduce(lambda x,y:y+x, s)
print(t)

# 将everyone替换成oldamy，可以用切片的方式替换吗？(注意:当有多个everyone怎么替换)
# 不可以
u = s.replace('everyone', 'oldamy')
print(u)

v = s[:20] + 'oldamy'
print(v)

# s[-9:] = 'oldamy'       # 'str' object does not support item assignment

# 6. 模拟命令行卸载模块(pip uninstall requests)
# 当输入y或Y提示进入卸载
# n或N提示退出程序
# 输入其它则提示输入不在选项范围之内

# ipt = input("请问您是否确认卸载程序?y/n")
# if ipt.upper() == 'Y':
#     print("你的程序已经卸载")
# elif ipt.upper() == 'N':
#     print("退出程序")
# else:
#     print("你输入的不在选项范围之内")

# 7. 输入用户名及密码
# 注意 用户名 以任意字符组成 但当用户输入包含空格的用户名将其去空格处理 并且 密码只能由数值及字母组成，否则提示格式不正确
# client = input("请输入用户名:")
# pwd = input("请输入密码(注意只能以数字和字母组成):")
# if pwd.isalnum() and ' ' not in client:
#     print('您的用户名:{},密码为:{}'.format(client, pwd))
# elif pwd.isalnum() and ' ' in client:
#     client = client.strip()
#     print('您的用户名:{},密码为:{}'.format(client, pwd))
# else:
#     print("你输入的密码格式不正确")


# 8. 实现将 'name = amy'字符串变为 "name ":" amy"
kw = 'name = amy'
kw = kw.split("=")
print('"'+kw[0]+'":"'+kw[1]+'"')

li = [1, 2, 3, 4]
# 9. 怎么在li后面添加 5,6,7,8四个元素(多种方式实现)
# li.append(int('5'))
# li.append(int('6'))
# li.append(int('7'))
# li.append(int('8'))
# print(li)

li.extend('5')
print(li)

# 10 del 与 li.clear()区别?
'''
clear() 函数用于清空列表内的元素,类似于 del a[:]
del()：删除指定值
'''
# del s
# print(s)
# 11. 将3改为"hello"是否可以更改?
li2 = ["hello" if i =='3'else i for i in li]
print(li2)
tu = (1, 2, 3, 4)
# 可以将3改为"hello"吗？ #  不可以
