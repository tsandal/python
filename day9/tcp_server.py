#import socket
#import time
#host = '0.0.0.0'
#port = 21567
#addr = (host, port)
##第一步：建立socket对象
#s = socket.socket()
##第二步：设置socket选项
#s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)        #这里value设置为1，表示将SO_REUSEADDR标记为TRUE，操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口，否则操作系统会保留几分钟该端口。
#第三步：绑定socket
#s.bind(addr)
##第四步：侦听连接。
#s.listen(2)#相当于有多少个客户端可以同时发送过来数据
##第五步：接受一个新连接
#cli_sock, cli_addr = s.accept()
#print('Client connected from:', cli_addr)
##第六步：用返回的套接字和客户端进行通信，接收和发送数据
## 将收到的bytes类型，转成utf8字符串
#data = str(cli_sock.recv(1024), encoding='utf8')
#data = '[%s] %s' % (time.strftime('%H:%M:%d'), data)
#print(data)
## 发送时，将utf8字符串转成bytes类型
#cli_sock.sendall(bytes(data, encoding='utf8'))
##第七步：关闭套接字
#cli_sock.close()
#s.close()

import socket

host = ''     # 代表0.0.0.0
port = 12345  # 应该大于1024
addr = (host, port)
s = socket.socket()  # 默认使用TCP协议
# 设置套接字选项，使得服务程序结束后可立即再启动
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)  # 一般只能写到5以内，表示允许多少客户端排队访问
cli_sock, cli_addr = s.accept()
print('客户端：', cli_addr)
data = cli_sock.recv(1024)  # 相当于fobj.read(1024)
print(data)
print(data.decode())
sdata = '欢迎!\r\n'
cli_sock.send(sdata.encode())   # 放送的数据必需是bytes类型，二进制
cli_sock.close()
s.close()
# yum install -y telnet
