# 1. while 循环
# 1.1 打印五次 hello jiajia
# i = 1
# while i <= 5:
#     i += 1          # 计数器
#     print("hello jiajia")

# 1.2 1-100之间的和
# i =1
# sum = 0
# while i <= 100:
#     sum = sum +i
#     i += 1
#     # i = 8退出循环
#     if i ==8:
#         # break退出循环体
#         # break             # 不会执行else,直接跳出循环
#         i = 101
#         # continue        # 跳出当前循环 进入下一次循环
#
# else:                       # 当while为false时执行else
#     # print(i)              # i =7
#     print(sum)              # 5050

# 1.3 直角三角形
'''
*
**
***
'''
# row = 1
# while row<= 4:
#     print('*'* row)
#     row += 1

# 嵌套循环
# row = 1
# while row <= 4:
#     stars = 1
#     while stars <= row:
#         print("*", end='')
#         stars += 1
#     row += 1
#     print()

