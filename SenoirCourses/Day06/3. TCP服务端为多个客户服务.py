'''
3. TCP服务端为多个客户端服务
'''


import socket


def main():
    # tcp的套接字
    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定信息
    tcp_server.bind(("192.168.0.161", 7890))

    # 为多个客户端服务，可以接听多个客户端
    while True:
        # 主动变被动
        tcp_server.listen(128)
        # accept() -> (socket object, address info)
        new_client_socket, client_addr = tcp_server.accept()
        # print(client_addr)

        # 为客户端多次服务，但是不能同时服务多个客户端，指不能同时回复客户端
        while True:
            # 接收数据  阻塞
            recv_data = new_client_socket.recv(1024)
            # print(recv_data)
            # recv_data解阻塞条件
            # 1.客户端发送过来数据
            # 2.客户端断开连接

            if recv_data.decode('gbk'):
                # 发送数据
                new_client_socket.send('haha'.encode('gbk'))
            else:
                break
        # 关闭客户端，截止为当前客户端服务
        new_client_socket.close()

    tcp_server.close()


if __name__ == '__main__':
    main()
