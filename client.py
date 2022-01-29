import socket

BUFSIZE = 1024

port = int(input('포트 번호: '))
address = ('localhost', port)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(address)

while True:
    msg = input('요청 메시지: ')
    sock.send(msg.encode())
    data = sock.recv(BUFSIZE)
    print("응답 메시지: {0}".format(data.decode()))
