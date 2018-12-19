import threading
import subprocess

def ping(host):
    rc = subprocess.call(
        'ping -c2 %s > /dev/null' % host,
        shell=True
    )
    if rc == 0:
        print('%s:up' % host)
    else:
        print('%s:down' % host)

if __name__ == '__main__':
    ips = ('172.40.58.%d' % i for i in range(1, 255))
    for ip in ips:
        t = threading.Thread(target=ping, args=(ip,))  # 创建工作线程
        t.start()  # target(ip) ==> target=ping
