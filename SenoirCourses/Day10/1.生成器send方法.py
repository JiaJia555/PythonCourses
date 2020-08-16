def create_num(num):
    a, b = 0, 1
    current_num = 0
    while current_num < num:
        result = yield a
        # print("result-->", result)
        a, b = b, a+b
        current_num += 1

    # return "jiajia"


g = create_num(5)
# for i in g:
#     print(i)

print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# 关闭生成器，不能运行
# g.close()
# 如果前面不调用next 第一次必须发送None
# print(g.send(None))             # 0
print(g.send('jiajia'))           # 1 与next类似
print(g.send('haha'))

# 打印return
# while True:
#     try:
#         ret = next(g)
#         print(ret)
#     except Exception as e:
#         print(e.value, "--")
#         break

# print(g.send(None))