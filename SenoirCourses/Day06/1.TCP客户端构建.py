'''
1.TCP客户端构建流程

创建socket
链接服务器
接收数据(最大接收2014个字节)
关闭套接字
'''
import socket
# from socket import *

def main():
    tcp_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # tcp_client = socket(AF_INET, SOCK_STREAM)
    server_ip = input('server ip')
    server_port = int(input("server port"))

    # 链接服务器
    tcp_client.connect((server_ip, server_port))

    # 发送数据
    send_data = input('发送数据')
    tcp_client.send(send_data.encode())
    # 接受数据,阻塞
    recedata = tcp_client.recv(1024)
    print(recedata.decode('gbk'))

    tcp_client.close()


if __name__ == "__main__":
    main()