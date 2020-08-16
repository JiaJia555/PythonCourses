# @ Time     : 2020/1/2
# @Author    : JiaJia
# 6.如何在环状数据结构中管理内存
# 当A被释放的时候，del方法会被执行
# class A:
#     def __del__(self):
#         print('del')
# a = 1
# a = A()

# 双向循环链表
# 双向链表也叫双链表，是链表的一种，它的每个数据结点中都有两个指针，
# 分别指向直接后继和直接前驱。所以，从双向链表中的任意一个结点开始，都可以很方便地访问它的前驱结点和后继结点。一般我们都构造双向循环链表。

import weakref
# 定义节点类
class Node:
    def __init__(self, data):
        # 定义数据域
        self.data = data
        # 定义左指向域
        self.left = None
        # 定义右指向域
        self.right = None

    def add_right(self, node):
        self.right = node
        # node.left = self
        node.left =weakref.ref(self)

    def __str__(self):
        return 'Node:<%s>' % self.data

    def __del__(self):
        print('in __del__: delete %s' % self)

def create_linklist(n):
    head = current = Node(1)
    for i in range(2, n + 1):
        node = Node(i)
        current.add_right(node)
        current = node
    return head

head = create_linklist(10)
head = None

import time
for _ in range(1000):
    time.sleep(1)
    print('run...')
input('wait...')

#虽然head = None, 运行上述代码之后并未执行del方法，这时候需要引入弱引用方法
# import 弱引用之后修改上面一行代码node.left即可
# 弱引用是不占用引用技术的
'''
在命令行输入
class A:
    def __del__(self):
        print('del')

import weakref
a = A
a2 = weakref.ref(a)
a3 = a2
del a
del a3
这个时候会输出del
'''