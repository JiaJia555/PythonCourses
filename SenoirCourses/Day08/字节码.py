'''
python字节码-->python虚拟机来执行python字节码
'''

import dis


def add_num(a):
    a += 1


print(dis.dis(add_num))

# 1 load a
# 2 load 1
# 3 执行add
# 4 赋值a
'''
0 LOAD_FAST                0 (a)
2 LOAD_CONST               1 (1)
4 INPLACE_ADD
6 STORE_FAST               0 (a)
8 LOAD_CONST               0 (None)
10 RETURN_VALUE
'''
