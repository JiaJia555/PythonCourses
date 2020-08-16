ipt = input("今天发工资了吗?y/n")
# if ipt.lower() == 'y':
#     print("ye!吃大餐")
# elif ipt.upper() =='N':
#     print('喝西北风')
# else:
#     print("到底发没发， 没有该选项")

if ipt.upper() == 'Y':
    salary = input("请问工资多少？")
    debt = input("请问前马哥多少？")
    remain = float(salary)-float(debt)
    print("no1: 还完马哥钱还剩{}".format(remain))
    if remain >= 1000:
        print("ye!吃大餐...")
elif ipt.upper() =='N':
    print("喝西北风")
else:
    print("到底发没发， 没有该选项")

