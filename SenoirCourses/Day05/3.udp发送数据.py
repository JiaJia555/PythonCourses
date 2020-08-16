# 3.udp发送数据
import socket

# 单次传送信息
def main():
    # 1. 创建udp套接字
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 发送数据
    # def sendto(self, data: bytes, address: _Address)
    # IP地址写localhost/127.0.1
    # udp_socket.sendto(b"jiajia", ('10.8.18.221', 8080))
    # 发送数据为中文, windows是gbk
    send_data = "佳佳"
    udp_socket.sendto(send_data.encode('gbk'), ('10.8.18.221', 8080))

    udp_socket.close()


if __name__ == '__main__':
    main()


# 多次传送信息
def main():

    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 没有绑定端口是随机分配的
    udp_socket.bind("", 49800)
    while True:
        send_data = input('请输入要发送的数据：')
        if send_data =='exit':
            break
        send_data = send_data.encode('gbk')
        udp_socket.sendto(send_data, ('10.8.18.221', 8080))
    udp_socket.close()


if __name__ =='__main__':
    main()

# 发送数据没有绑定端口前是随机分配的
'''
1. 127.0.0.1/8整个都是环回地址，用来测试本机的TCP/IP协议栈，发往这段A类地址数据包不会出网卡，网络设备不会对其做路由。
2. localhost  就是个指向本机环回口的域名，方便记忆与输入，
3. 本机IP=内网IP
4. 外网IP是整个因特网的地址，唯一的，没有重复的
内网ip是局域网内的IP地址，只能使用局域网内部资源，如果要使用因特网的资源则需要有外网IP作为出口，
不同的内网可以重复使用IP，例如A网有192.168.0.1，B网同样可以有，不冲突。
'''