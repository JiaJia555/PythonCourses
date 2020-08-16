# 2.输入与输出
# 2.1 input()输入函数不论输入什么返回值都为字符串
a = input('请输入')  # 输入11，
print(type(a))       # <class 'str'>
# 当不输入任何值时，输出的是空的字符串
# 输出值会保留原有输入值的格式，包括空格

# eg:输入年龄,判断年龄>18则输出”你好呀,小靓仔”；否则输出”你好呀！小朋友”
age = input("请输入你的年龄")   # input输入的一定是字符串
# 判断是否全为数字
if age.isdigit():
    if int(age) > 18:  # 比较的是int
        print("你好，小靓仔")
    else:
        print("你好呀，小朋友")
else:
    print("hello你输入的不是整数！")

# 2.2 当程序中有input()函数时,程序会停止在input()函数这块,这是程序阻塞
print("开始")
input("阻塞中")
print("结束")

# 3.print函数
# print(self, *args, sep=' ', end='\n', file=None)
# end 默认换行
print("hello world", "xiaoxiao", sep=",")   #输出为 hello world,xiaoxiao
print("hello JiaJIa")
