'''
5. TCP客户端

socket创建套接字
bind绑定IP和port
listen使套接字变为可以被动链接
accept等待客户端的链接
recv/send接收发送数据
'''
import socket


def send_file_client(new_client_socket):
    # 接收口红的发送过来的数据
    file_name = new_client_socket.recv(1024).decode()

    content = b""

    try:
        with open(file_name, 'rb') as f:
            content = f.read()
    except:
        print("no download file:%s" % file_name)

    new_client_socket.send(content)

    new_client_socket.close()


def main():

    tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    tcp_server_socket.bind(("", 8080))

    tcp_server_socket.listen(128)

    new_client_socket, client_addr = tcp_server_socket.accept()

    # 给客户端返回文件内容
    send_file_client(new_client_socket)

    tcp_server_socket.close()

if __name__ == '__main__':
    main()
