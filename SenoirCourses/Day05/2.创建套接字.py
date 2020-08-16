# 2.创建套接字

import socket

# from socket import socket

# 1.创建套接字
# family = AF_INET,     协议族 AF_INET ipv4,
# type=SOCK_STREAM      套接字类型 TCP 流式套接字; UDP: SOCK_DGRAM 数据报套接字
# AF_INET = 2
# AF_INET6 = 23
s = socket.socket(family=socket.AF_INET, tyep=socket.SOCK_DGRAM)

# 2.使用套接字 收/发 数据
# udp 类似寄送信件，不安全，不能确保一定收到，也不能确定对方是否收到邮件
# tcp 能知道对方是否收到信息，更安全，类似打电话
# 3.关闭套接字
s.close()

# 和文件操作流程类似