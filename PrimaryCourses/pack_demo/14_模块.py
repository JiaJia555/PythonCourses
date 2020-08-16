import time
# print("111")
# time.sleep(4) #延迟执行时间：秒
# print("2222")

# print(time.time())  # 1970年至今的时间戳(s)

# print(time.localtime())  # 本地时间: tuple

# print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))
# import datetime  # (看源码)
# print(datetime.datetime.now())  #小数点精确度不能改变

'''
random
'''
import random
# print(random.random()) #随机数(0,1],左闭右开
# print(random.randint(1, 10))  # 随机取整[a,b]
# s = "hello"
# print(random.choice(s))  # 随机在序列中取元素

# li = [1, 2, 3, 2, 34, 5]  # 可变列表
# random.shuffle(li)  # 洗牌，对Li本身进行操作的 list
# print(li)

# li = [5, 6, 5, 1, 4, 5]
# print(random.sample(li, 2))

# print(random.randrange(1, 10))  # range() [)

'''
字母+数字随机组合的验证码 5
'''


# def ver_code():
#     code = ''
#     for i in range(5):
#         digi = str(random.randrange(10))
#         alp = chr(random.randrange(65, 91))
#         num = random.choice([digi, alp])
#         code += num
#     print(code)
#
# ver_code()

# 65-90 A-Z 数值通过ascII转为字母
# print(chr(90))

'''
正则表达式
re.findall(pattern, string, flags=0) 匹配所有
pattern 匹配的正则表达（模式）
string 要匹配的字符串
flags 标志位（是否区分大小写，多行匹配）
'''

import re
s = "python, ipython"
# res = re.findall("py", s)  # []
# res1 = re.findall('ipy', s)
# res2 = re.findall('^p+', s)
# print(res)
# print(res1)
# print(res2)

# print(re.findall(".", 'abc'))  # .代表所有字符，['a', 'b', 'c']
# print(re.findall('a.c', 'a\nc'))  # []
# print(re.findall('a.c', 'a\nc', flags = re.DOTALL))  # ['a\nc']

# (a|b)c --> ac, ab
# print(re.findall('a[cm]y', 'amy'))  # ['acy'] ['amy']
# print(re.findall('a[a-z,1-9]y', 'a,y'))
# print(re.findall('a[-a-z1-9]y', 'a-y'))
# print(re.findall('[A-Za-z1-9]', 'hsidchsadiu5454'))
#只匹配一个
'''
\转义字符
\跟元字符搭配-->去除特殊功能 \.-->普通字符
\普通字符搭配-->实现特殊功能 t-->\t 特殊字符
'''
# s = '.1'
# print(re.findall('\.', s))
'''
匹配一个数字[0-9] 字母[a-z]
[^0-9]-->[^] -->0-9范围之外的都可
'''
# print(re.findall('[a-z]', 'A'))

# print(re.findall('\d{11}', '15200806666'))
# print(re.findall('\d+', '15200806666'))  # +-->{1,}
# print(re.findall('\w*', '111aaaa00806666'))  # *-->{0,}
# print(re.findall('\d*', 'aaaa00806666'))  # {0,}
# print(re.findall('\d+?', '15200806666'))

'''
re.search()返回的是一个对象,group()
只匹配一个，就不会往下找了
'''
# print(re.search('py', 'python, ipython').group())
# print(re.search('py', 'hon'))  # 输出None
# print(re.search('py', 'python').group())

'''
re.match() 只在字符串开始匹配 返回也是对象 group()调用
'''
# print(re.match('asd', 'asdhshjaasd').group())
# print(re.match('asd', 'aaaasdhshjaasd').group()) # 报错

'''
re.split() 重点
'''
print(re.split('p', 'ipythonpython'))
print(re.split('[p,h]', 'ipythonpython'))  # 多个拆分

'''
re.sub() 相当于replace, 替换
'''
res = re.sub('w...d', 'amy', 'hello world') # 指定从什么开始什么结束
print(res)

'''
re.compile()
1. 转为正则对象
2. 重复使用一个规则
'''
obj = re.compile('\.com')
print(obj.findall('shiuashi.com'))
print(obj.findall('shiuashi.com'))


