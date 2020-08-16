import time
'''
避免重复造轮子
'''
# def test2():
#     start = time.time()
#     print("----1----")
#     time.sleep(1)
#     end = time.time()
#     print("花了{}".format(end-start))
#
# def test3():
#     start = time.time()
#     print("----1----")
#     time.sleep(1)
#     end = time.time()
#     print("花了{}".format(end-start))
'''
开放：拓展其他功能
封闭：不要修改封装好的代码块
原则
'''
# def calcu_time(func):
#     def test_in():
#         start = time.time()
#         func()
#         end = time.time()
#         print("花了{}".format(end - start))
#     return test_in

# @calcu_time             # test2 = calcu_time(test2)
# def test2():
#     print("----2----")
#     time.sleep(1)
# test2 = calcu_time(test2)           # test2 = test-in  test1改名字怎么办
# test2()                 # test2() test_in()

# @calcu_time             # test2 = calcu_time(test2)
# def test3():
#     print("----3----")
#     time.sleep(1)
#
# test2()
# test3()

'''
加验证
'''
def outer(flag):
    def calcu_time(func):
        def test_in():
            start = time.time()
            func()
            end = time.time()
            print("花了{}".format(end - start))
            if flag == 'true':
                print("正在验证")
        return test_in
    return calcu_time


@outer(flag="true")     # calcu_time= outer()  test2 = calcu_time(test2)
def test2():
    print("----1----")
    time.sleep(1)


test2()
# res = calcu_time(test2)
# res()  # test2() test_in()