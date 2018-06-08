#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Zhangsiqi
#   Date    :   18/6/6
#   Desc    :   传送字符串的阻塞 server
#服务器端的socket对象，listen_socket 从不和客户端交换数据。它只会通过accept方法接受连接。然后，创建一个新的socket对象，client_connection用于和客户端通信。服务器端的socket 分为：接受请求的socket（listen_socket） 和 与客户端传输数据的socket（client_connection）
import socket
import time

SERVER_ADDRESS = (HOST, PORT) = '192.168.123.7', 6666#把服务器的地址和端口号赋给SERVER_ADDRESS
REQUEST_QUEUE_SIZE = 5


def handle_request(client_connection):#处理请求
    while 1:#可以一直显示客户端传送的字符串
        request = client_connection.recv(1024)#接收客户端client传来的字符串
    	print('Server recv: {request_data}'.format(request_data=request.decode()))#显示客户端client传来的字符串
    	time.sleep(5)  # 模拟阻塞事件，等待5s
    	if request == "Hello, I'm client:exit":#如果客户端client传来的字符串是"Hello, I'm client:exit"
            print 'Connection close'
            client_connection.send('Connection closed!')#向客户端传送字符串'Connection closed!'
            break#终止循环语句
    	http_response = "Hello, I'm server"
    	client_connection.sendall(http_response)#向客户端传送字符串"Hello, I'm server"


def server():
# server 端创建一个socket,linux系统会分配唯一一个socket 编号给它  
# socket.AF_INET --> 机器网络之间的通信  
# socket.SOCK_STREAM --> TCP 协议通信(对应UDP)  
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# 把服务绑定到对应的ip和port 
    listen_socket.bind(SERVER_ADDRESS)
# 启动socket 网络监听服务,一直监听client的网络请求
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Server on port {port} ...'.format(port=PORT))

    while 1:
        client_connection, client_address = listen_socket.accept()
        handle_request(client_connection)
# 通信完毕，关闭链接；链接没有关闭时可进行可以多次数据通信 
        client_connection.close()

if __name__ == '__main__':
    server()
