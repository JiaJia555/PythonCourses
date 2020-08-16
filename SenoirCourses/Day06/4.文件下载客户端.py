'''
4. TCP客户端

创建套接字
连接服务器

要下载的文件名称
发送文件下载的请求
接收服务端发送过来的数据
保存文件

关闭套接字
'''
import socket


def main():
    # 创建套接字
    tcp_client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # server_ip = input("server ip:")
    # server_port = int(input("server port:"))

    #连接服务器
    # tcp_client_socket.connect((server_ip, server_port))
    tcp_client_socket.connect(('10.9.45.127', 8080))


    file_name = input("请输入文件名称")

    # 发送文件下载请求
    tcp_client_socket.send(file_name.encode('gbk'))
    # 接收文件
    recv_data = tcp_client_socket.recv(1024*1024)

    if recv_data():
        # 保存文件
        with open("接收"+ file_name, "wb") as f:
            f.write(recv_data)



if __name__ == '__main__':
    main()





