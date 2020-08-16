#1. 过滤掉该列表names = ["Ellen","OldLi","Amy","Wendy","Tom","Bob"]
#长度小于或等于3 的字符串列表，并将剩下的转换成大写字母。
#names = ["Ellen","OldLi","Amy","Wendy","Tom","Bob"]
#new_names = [name.upper() for name in names if len(name)>3]
#print(new_names), 只有当条件满足才会保留下来
'''
for name in names:
    if len(name)>3:
        names.append(name)
print(names)
'''
#2. 求(x,y),其中x 是0-5 之间的偶数，y 是0-5 之间的奇数组成的元祖
#列表
# lis = [(i, j) for i in range(5) if i%2 == 0 for j in range(5) if j%2 == 1]
# print(lis)
#3. res = [lambda x:x+i for i in range(10)]，res[0](10)结果是多少，为什么?
# res = [lambda x:x+i for i in range(10)]
# print(res[0](10))
#输出为19，闭包函数理解一下
#4. tu = (i for i in range(20))这是元组推导式吗？---元组没有推导式
# tu = (i for i in range(20))
# print(tu)
#print(tuple(tu))

#5. student = {"name":"OldZhang","age":"22","gender":"male"} 将
# #key,value 互换
#student = {"name":"OldZhang","age":"22","gender":"male"}
# new_student= {value: key for key,value in student.items()}
# print(new_student)
# student_rever = {v:k for k,v in student.items()}
# print(student_rever)

#6. ["Ellen","OldLi","Amy","Wendy","Tom","Bob"]将该列表实现{0: 'Ellen',
#1: 'OldLi', 2: 'Amy', 3: 'Wendy', 4: 'Tom', 5: 'Bob'} 注意: 此处可用到
#enumerate 方法
#list6 = ["Ellen","OldLi","Amy","Wendy","Tom","Bob"]
# for index, item in enumerate (list6):
#     print (index, item)

# dic1 = {k:v for k,v in enumerate(list6)} #答案
# print(dic1)

#7. [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'James', 'Bob','JAMES','jAMeS' ]该
#列表很紊乱，实现去重,以及将名字格式统一成首字母大写
names = [ 'Bob', 'JOHN', 'alice', 'bob', 'ALICE', 'James', 'Bob','JAMES','jAMeS' ]
# list7 = []
# for i in names:
#     if i not in list7:
#         list7.append(i)
# print(list7) #为什么去重失败
#print(list(set(names)))#这个为什么也不行呢，

# s1 = {i.capitalize() for i in names} #答案
# print(s1) #set 有去重功能