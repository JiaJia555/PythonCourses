# 4.udp接收数据
'''
1 创建套接字
2 绑定本地信息(IP和端口)
3 接受数据
4 打印数据
5 关闭套接字
'''
import socket
def main():
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 不写ip表示本机任何ip地址
    bind_addr = ('', 7789)  # 7789是远程主机，发送者的端口
    udp_socket.bind(bind_addr)

    while True:
        # 1024表示本次接收的最大字节数
        recv_data = udp_socket.recvfrom(1024)  # 字节大于1024报错
        # print(recv_data)  # 中文不可以
        # (b'1', ('10.8.18.221', 8080))
        # 元组 接收到的数据 （发送方的ip和端口）

        message = recv_data[0]    # 接收到的数据
        address = recv_data[1]    # 发送方的地址
        print('%s:%s'%(str(address), message.decode('gbk')))
        # ('10.8.18.221', 8080):嘉佳

    udp_socket.close()

if __name__ == '__main__':
    main()



