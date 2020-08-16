# 5. 多任务版udp聊天
'''
1 创建套接字
2 绑定本地信息
3 获取对方IP和端口
4 发送、接收数据
5 创建两个线程，去执行功能
'''
import socket
import threading


def recv_msg(udp_socket):
    """接收数据"""
    while True:
        recv_data = udp_socket.recvfron(1024)
        print(recv_data)


def send_msg(udp_socket, dest_ip, dest_port):
    """发送数据"""
    while True:
        send_data = input("请输入要发生的数据")
        udp_socket.sendto(send_data.encode('gbk'), (dest_ip, dest_port))
        # 报错，因为接收和发送数据不能同时运行，这个时候可以试试多线程


def main():
    """完成udp聊天器"""
    # 创建套接字
    udp_socket = socket.socket(socket.AF_INET, socket.sock_DGRAM)
    # 绑定
    udp_socket.bind(("", 7890))

    # 获取对方的IP和端口
    dest_ip = input("请输入对方的IP")
    dest_port = int(input("请输入对方的port:"))

    # 接收数据
    # while True:
    #     recv_data = udp_socket.recvfron(1024)
    #     print(recv_data)

    # 发送数据
    # while True:
    #     send_data = input("请输入要发生的数据")
    #     udp_socket.sendto(send_data.encode('gbk'), (dest_ip, dest_port))
        # 报错，因为接收和发送数据不能同时运行，这个时候可以试试多线程

    t_recv = threading.Thread(target=recv_msg, args=(udp_socket,))
    t_send = threading.Thread(target=send_msg, args=(udp_socket, dest_ip, dest_port))

    t_recv.start()
    t_send.start()


if __name__ == "__main__":
    main()