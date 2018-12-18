import socket
host='127.0.0.1'
port=12345
addr=(host,port)
c=socket.socket()
c.connect(addr)
c.send(b'Hello world\r\n')
data=c.recv(1024)
print(data.decode(),end='')
c.close()
