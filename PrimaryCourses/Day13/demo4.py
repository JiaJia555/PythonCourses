# import demo3  # pycharm默认在用户名文件夹下
#
# demo3.test()
# demo3.test1()

# from demo3 import test, test1  #命名冲突
# from demo3 import test1
#
# def test():
#     print('demo4.test')
# test()
# test1()

# from demo3 import test as demo3_test
# from demo3 import test1 as demo3_test1
#
#
# def test():
#     print('demo4.test')
#
# demo3_test()
# test()
# demo3_test1()

from demo3 import *

test()
test1()

# if __name__ == '__main__':
