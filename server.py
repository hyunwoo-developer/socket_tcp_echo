import select
from socket import *

PORT = 8080
BUFSIZE = 1024

with socket(AF_INET, SOCK_STREAM) as s:
    s.bind(('localhost', PORT))
    s.listen(1)
    print('서버가 시작되었습니다.')

    readsocks = [s]

    while True:
        readables, writeables, exceptions = select.select(
            readsocks, [], [])
        for sock in readables:
            if sock == s:
                newsock, addr = s.accept()
                print('클라이언트 접속: ', addr)
                readsocks.append(newsock)
            else:
                conn = sock
                data = conn.recv(1024)
                print('받은 메시지: ', data.decode())
                conn.send(data)
                if data.decode() == "exit":
                    conn.close()
                    readsocks.remove(conn)
