# 4. 代码调试和性能分析
# 4.1 代码调试
import pdb
a = 1
b = 2

def func():
    print('enter func()')


pdb.set_trace()
c = 3
func()
print(a + b + c)

# 输入n 代表继续往下运行
# p 代表打印
# l查看上下文代码
# return 代表程序结束了，再按n就会报错
# s 代表进入到方法内部
# q 退出
# https://docs.python.org/3/library/pdb.html#module-pdb%EF%BC%89

# 4.2 用 cProfile 进行性能分析
# profile是指对代码的每个部分进行动态的分析，比如准确计算出每个模块消耗的时间等。

import cProfile
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fib_seq(n):
    res = []
    if n > 0:
        res.extend(fib_seq(n-1))
    res.append(fib(n))
    return res


print(fib_seq(30))
cProfile.run('fib_seq(30)') # 括号里面是str, 输出结果如下
'''
ncalls  tottime  percall  cumtime  percall filename:lineno(function)
7049123/31    2.092    0.000    2.092    0.067 4.代码调试.py:27(fib)
     31/1    0.000    0.000    2.092    2.092 4.代码调试.py:35(fib_seq)
        1    0.000    0.000    2.092    2.092 <string>:1(<module>)
        1    0.000    0.000    2.092    2.092 {built-in method builtins.exec}
       31    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
       30    0.000    0.000    0.000    0.000 {method 'extend' of 'list' objects}

参数介绍：

ncalls，是指相应代码 / 函数被调用的次数
tottime，是指对应代码 / 函数总共执行所需要的时间（注意，并不包括它调用的其他代码 / 函数的执行时间）
tottime percall，就是上述两者相除的结果，也就是tottime / ncalls
cumtime，则是指对应代码 / 函数总共执行所需要的时间，这里包括了它调用的其他代码 / 函数的执行时间
cumtime percall，则是 cumtime 和 ncalls 相除的平均结果。
'''
# 案例，阶乘

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return (n*factorial(n-1))

a = factorial(5)
print(a) # 120
cProfile.run('print(a)')

'''
 ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {built-in method builtins.print}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
'''