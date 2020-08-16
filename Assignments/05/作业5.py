# 1.遍历"12",遍历range(12)
# for i in '12':
#     print(i)
#
# for i in range(12):
#     print(i)
# 2.计算10的阶乘
# factorial = 1
# for i in range(1, 11):
#     factorial *= i
# print(factorial)
#
# f = 1
# i =1
# while i <= 10:
#     f *= i
#     i += 1
# print(f)
# 3.计算从1-1000以内的所有奇数的和并输出
# s = 0
# i = 1
# while i <= 1000:
#     s += i
#     i += 2
# print(s)

s = 0
for i in range(1, 1000, 2):
    s += i
print(s)

# 4.打印出所有的"水鲜花数"，所谓"水鲜花数"是指一个三位数，其个位数字
# 立方和等于该数本身。例如：153是一个"水仙花数" 1^3 + 5^3 +3^3 = 153
for i in range(100, 1000):
    if (i//100)**3 + ((i%100)//10)**3 + (i%10)**3 ==i:
        print(i)
# 5. 定义一个函数，完成用户输入的三个数字的求和 以及在另一个函数求该
# 和的平均值


def sum(x, y, z):
    res = x + y + z
    print("{} = {} + {} + {}".format(res,x,y,z))


def avg_num(x, y, z):
    res = (x + y + z)/3
    print("{} = ({} + {} + {})的平均值".format(res,x,y,z))


if __name__ == '__main__':
    x = int(input("请输入第一个字："))
    y = int(input("请输入第一个字："))
    z = int(input("请输入第一个字："))
    sum(x, y , z)
    avg_num(x, y, z)