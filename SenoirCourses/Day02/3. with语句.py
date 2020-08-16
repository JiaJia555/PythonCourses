# @ Time     : 2020/1/2
# @Author    : JiaJia
# 3.with 语句
try:
    f = open('test.txt', 'w')
    # print("code")
    raise KeyError
except KeyError as e:
    print('Key Error')
    f.close()
except IndexError as e:
    print("IndexError")
    f.close()
except Exception as e:
    print(e)
    f.close()
finally:
    # 不管有没有异常都会运行
    print('end')
    f.close()

# with 语句自动关闭
# with open('demo.txt', 'r') as f:
#     f.read()
# 3.1 类的with 语句，上下文管理器，可简化异常处理


class Sample(object):
    # 1.获取资源
    def __enter__(self):
        print('start')
        return self
    # 处理资源
    def demo(self):
        print('this is demo')

    # 3.释放资源
    def __exit__(self, exc_type, exc_val, exc_tb):
        # <class 'AttributeError'> 异常类
        print(exc_type, '_')
        # 'Sample' object has no attribute 'dems' 异常值
        print(exc_val, '_')
        # <traceback object at 0x0000003DC40B7BC8> 追踪信息
        print(exc_tb, '_')
        print('end')


with Sample() as sample:
    sample.demo()  # this is demo

# 3.2 contextlib简化上下文管理器
import contextlib


@contextlib.contextmanager
def file_open(filename):
    # xxx __enter__函数
    print("file open")
    yield{}  # 不可以用return
    # __exit__函数
    print('file close')


with file_open("demo.txt") as f:
    print('file operation')






