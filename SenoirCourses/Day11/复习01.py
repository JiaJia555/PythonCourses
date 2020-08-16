'''
### 1.如何区别可变数据类型和不可变数据类型
对象的内存地址方向
- 可变数据类型
- 内存地址不变
值是可以改变的, list
dict
set
- 不可变数据类型
- 内存地址改变, 值也跟着变化, int
str
tuple
布尔

### 2.Python 垃圾回收机制？
s = 1

s = 'juran'
- 引用计数机制
- 循环引用
- 标记 - 清除
- 分代回收

### 3. Python中会有函数或成员变量包含单下划线前缀和结尾，和双下划线前缀结尾，区别是什么?
- __私有成员
- _保护变量

### 4.如何判断一个对象是函数还是方法？
from type import MethodType, FunctionType

class Demo(object):
    def foo(self):
        pass
def foo2():
    pass

print(isinstance(Demo().foo,FunctionType))  # False
print(isinstance(Demo().foo,MethodType))  # True
print(isinstance(foo2.foo,FunctionType))  # True
print(isinstance(foo2.foo,MethodType))      # False

### 5. super函数的用法
- 调用父类中的方法
实际按照mro算法调用

class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print("C")

class D(B,C):
    def __init__(self):
        print("D")
if __name__ == '__main__':
    d = D()
    print(D.__mro__)        # D B C A

### 6.使用isinstance和type的区别
- isinstance考虑类的继承关系
- type不会考虑类的继承关系

### 7.创建大量实例节省内存
```
__slots__ = []()
单例模式 - 只实例化一次
```

### 8.上下管理器
```
__enter__
__exit__
```
class Sample(object):
    def __enter__(self):
        # 获取资源
        print("start")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 释放资源
        print('end')
        # 异常

    def demo(self):
        print('demo')


with Sample() as f:
    f.demo()
# with 自动关闭

### 9.判断一个对象中是否具有某个属性
- hasattr(object, name)
class Demo(object):
    name = 'jiajia'
    def run(self):
        return'hello'
d = Demo()

print(hasattr(d, 'name'))    # True
print(hasattr(d, 'run'))        # True
print(hasattr(d, 'age'))        # False

### 10.property动态属性的使用
- 装饰器
- get
set
Day04 2属性描述符
class C(object):
    @property
    def x(self):
        "I am the 'x' property."
        return self._x

    @x.setter
    def x(self, value):
        self._x = value

    @x.deleter
    def x(self):
        del self._x

### 11.如何使用type创建自定义类
```
type(name, bases, attr)
name 表示类名称 字符串
bases 继承对象的元组
attr 属性 类属性 类方法 静态方法 字典
```

### 12.生成器的创建
-
yield
- ()
send 方法
- next
- send
- 如果前面没有调用next的情况下, 第一次必须传None

### 13.TCP 和 UDP 的区别？
- TCP面向连接
UDP是无连接
- TCP安全可靠
UDP 不保证可靠
- UDP实时性
- TCP是点到点
UDP
支持一对一
一对多
- TCP对系统资源要求较多

### 14.TCP服务端通信流程
- 创建socket套接字
- 绑定IP和PORT
- listen
- accept等待客户端连接
- 收发数据

### 15.创建线程的两种方式
- 普通创建
threading
- 类的继承
threading.Thread

### 16.解释线程资源竞争,以及解决方案
共享资源，所以有竞争
a += 1
```
创建锁
mutex = threading.Lock()
mutex = threading.RLock()  可重入的锁 多次上锁

mutex.acquire()   加锁
mutex.release()   解锁
```

### 17.进程之间的通信,以及进程池中的进程通信
进程之间的通信
multiprocessing.queue
进程池中的进程通信
multiprocessing.Manger.Queue
队列先进先出
### 18. 同步、异步、阻塞、非阻塞
同步：代码在IO操作必须等待上一个操作完成，有顺序的
异步：可以同时执行
阻塞：input
非阻塞: print
### 19.进程、线程、协程对比
- 进程是资源分配的单位
- 线程是操作系统调度的单位
- 进程切换需要的资源比较大
- 进程可以发现多核的优势
'''