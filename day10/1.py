import os
#print('start')
#os.fork()
#print('hello')

print('start')
a=os.fork()
if a:
    print('in parent')
else:
    print('in child')
print('end')

import os
import time
from datetime import datetime
pid = os.fork()
if pid:
    print("In parent!")
    time.sleep(10)
    print("parent exit")
else:
    for i in range(5):
        print(datetime.now())
        time.sleep(1)
    print("child exit")

import subprocess        #加载支持Linux系统内部命令模块
import os
#定义函数，允许ping任何主机，ping函数需要给IP作为参数
def ping(host):
    rc = subprocess.call(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )            #定义ping命令的变量，返回值0:正常，返回值1：ping不通
    if rc:
        print('%s: down' % host)    #无法ping通打印down
    else:
        print('%s: up' % host)        #当re=0，表示可以ping通，打印up
if __name__ == '__main__':
    #生成整个网段的IP列表[172.40.58.1,172.40.58.2....]
    ips = ['172.40.58.%s' % i for i in range(1, 255)]
    for ip in ips:
        pid = os.fork()    # 父进程负责生成子进程
        if not pid:    # 子进程负责调用ping函数
            ping(ip)
            exit()        # 子进程ping完一个地址后结束，不要再循环




import socket
import os
from time import strftime
class TcpTimeServer:
    def __init__(self, host='', port=21567):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)
    def chat(self, c_sock):
        while True:
            data = c_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode('utf8'))
            c_sock.send(data.encode('utf8'))
        c_sock.close()
    def mainloop(self):
        while True:
            cli_sock, cli_addr = self.serv.accept()
            pid = os.fork()
            if pid:
                cli_sock.close()
#取出waitpid元组中第一个数，优先处理僵尸进程
#waitpid()的返回值：如果子进程正在运行、尚未结束则返回0，否则返回子进程的PID
                while True:
                    result = os.waitpid(-1, 1)[0]
                    if result == 0:
                        break
            else:
                self.serv.close()
                self.chat(cli_sock)
                exit()
        self.serv.close()
if __name__ == '__main__':
    s = TcpTimeServer()
    s.mainloop()





import subprocess
import threading
def ping(host):
    rc = subprocess.call(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )
    if rc:
        print('%s: down' % host)
    else:
        print('%s: up' % host)
if __name__ == '__main__':
    ips = ['172.40.58.%s' % i for i in range(1, 255)]
    for ip in ips:
        # 创建线程，ping是上面定义的函数, args是传给ping函数的参数
        t = threading.Thread(target=ping, args=(ip,))
        t.start()  # 执行ping(ip)



import threading
import subprocess
class Ping:
    def __init__(self, host):
        self.host = host
    def __call__(self):
        rc = subprocess.call(
            'ping -c2 %s &> /dev/null' % self.host,
            shell=True
        )
        if rc:
            print('%s: down' % self.host)
        else:
            print('%s: up' % self.host)
if __name__ == '__main__':
    ips = ('172.40.58.%s' % i for i in range(1, 255))  # 创建生成器
    for ip in ips:
        # 创建线程，Ping是上面定义的函数
        t = threading.Thread(target=Ping(ip))  # 创建Ping的实例
        t.start()   #执行Ping(ip)



import socket
import threading
from time import strftime
class TcpTimeServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)
    def chat(self, c_sock):
        while True:
            data = c_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (strftime('%H:%M:%S'), data.decode('utf8'))
            c_sock.send(data.encode('utf8'))
        c_sock.close()
    def mainloop(self):
        while True:
            cli_sock, cli_addr = self.serv.accept()
            t = threading.Thread(target=self.chat, args=(cli_sock,))
            t.start()
        self.serv.close()
if __name__ == '__main__':
    s = TcpTimeServer()
    s.mainloop()






