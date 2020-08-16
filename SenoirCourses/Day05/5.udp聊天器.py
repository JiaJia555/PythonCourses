# 5 聊天器
import socket

def send_data(udp_socket):  # 传参
    """发送数据"""
    send_data = input('请输入要发送的数据')
    dest_ip = input("请输入要发送的IP:")
    dest_port = int(input("请输入要发送的端口:"))
    udp_socket.sendto(send_data.encode('gbk'), (dest_ip, dest_port))

def recv_data(udp_socket):
    """接收数据"""
    recv_data = udp_socket.recvfrom(1024)
    print("%s:%s" % (recv_data[1], recv_data[0].decode('gbk')))

def main():
    #创建套接字，同时接收和发送
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 绑定端口
    udp_socket.bind(('', 1234))   # ''默认本地ip

    while True:
        # 发送
        send_data(udp_socket)
        # 接收
        recv_data(udp_socket)

    udp_socket.close()


if __name__ == '__main__':
    main()