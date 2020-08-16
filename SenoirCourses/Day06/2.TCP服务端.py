'''
2. TCP服务端

1 socket创建套接字
2 bind绑定IP和port     固定的
3 listen使套接字变为可以被动链接
4 accept等待客户端的链接
5 recv/send接收发送数据

1 买手机
2 插上手机卡
3 设置手机为正常接听状态
4 等待别人打电话
'''
import socket


def main():
    # tcp的套接字，负责等待新的客户链接
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定信息
    tcp_server.bind(('10.9.45.127', 8080))

    # 主动变被动
    tcp_server.listen(128)

    print("--1--")
    # accept() -> (socket object, address info)  # 新的套接字和客户端地址
    new_client_socket, client_addr = tcp_server.accept()  # 新的套接字服务客户端，会阻塞到客户端连接
    # print(client_addr)
    print("--2--")
    # 接收数据
    recv_data = new_client_socket.recv(1024) # 阻塞到客户端发送数据
    print(recv_data)

    # 发送数据
    new_client_socket.send('haha'.encode('gbk'))

    # 关闭套接字
    new_client_socket.close()
    tcp_server.close()


if __name__ == '__main__':
    main()
