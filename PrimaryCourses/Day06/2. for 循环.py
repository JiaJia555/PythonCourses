'''
for i in iterable:
    pass
'''
# list()
# str()
# tuple()
# dict()
# range()
# int()

# print(list(range(1, 10, 2)))          # 左闭右开

lis = [1, 2, 3]
lis_iter = lis.__iter__()               # 转化为迭代器
# print(lis_iter)
# __next__
# try:
#     while True:
#         print(lis_iter.__next__())
# except StopIteration:
#     pass

# 12 返回 壹拾贰元整
# 长度2
# ch_num[1] ch[len(2)-1]  ch_num[2] ch[len(2)-1-1]
# ch_num = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
# ch = ['圆', '拾', '佰', '仟', '萬']
#
# ipt = input("请输入数字:")
# len_ipt = len(ipt)
# for i in ipt:
#     len_ipt -= 1
#     # # print(i)
#     # print(ch_num[int(i)])
#     # print(ch[len_ipt])
#     # # print(ch[len_ipt - 1])
#     # # print(ch[len_ipt - 1])
#     print("{}".format(ch_num[int(i)]), ch[len_ipt], end='')

# 九九乘法表
'''
1*1 = 1
2*1 = 2  2*2 = 4
...
'''
flag = False
for i in range(1, 10):
    # if i == 4:
    #     break
    # print(i)
    if flag:
        break
    for j in range(1, i+1):
        if j == 3:
            flag = True
            # break
        # print(i, j)
        print("{}*{}={}".format(j, i, (j*i)), end=' ')
    print("")

for i in range(1, 10):
    if i == 8:
        # break       # 输出到7停止
        continue      # 输出7，跳过8，再输出9
    print(i)



