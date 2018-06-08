#!/usr/bin/env python
# -*- coding:utf-8 -*-
#
#   Author  :   Zhangsiqi
#   Date    :   18/6/6
#   Desc    :   传送字符串的非阻塞 client

import socket

SERVER_ADDRESS = (HOST, PORT) = '192.168.123.7', 8888#把服务器的地址和端口号赋给SERVER_ADDRESS

def send_message(s, message):#发送请求，把message的信息发给s，用到的是sendall函数
    s.sendall(message)


def client():
# socket.AF_INET --> 机器网络之间的通信  
# socket.SOCK_STREAM --> TCP 协议通信(对应UDP)  
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(SERVER_ADDRESS)#与server端连接
    while 1:
        message = "Hello, I'm client:"
	mess = raw_input('Input client name: ')
        message=message+mess
	send_message(s, message)
	print (mess),'is waiting response...'
	data = s.recv(1024)#recv函数接收server端发过来的数据
        if mess == 'exit':
            break
    s.close()
    print (mess),'recv:', repr(data)  # 打印从服务器接收回来的数据

if __name__ == '__main__':
    client()

