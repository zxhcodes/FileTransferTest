import time
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM
from socketserver import BaseRequestHandler, TCPServer, UDPServer


class TcpFileHandler(BaseRequestHandler):
    def handle(self):
        print("start recv...")

        totals = 0
        beg = time.time()

        while True:
            chunk = self.request.recv(1024 * 1024)
            if not chunk:
                break
            totals += len(chunk)

        print(time.time()-beg, totals)

        print("over")

def recv_by_tcp():
    with TCPServer(('', 8080), TcpFileHandler) as serv:
        serv.serve_forever()


class UdpFileHandler(BaseRequestHandler):
    beg = 0
    totals = 0
    def handle(self):
        msg, sock = self.request
        if msg == b'0':
            print("start recv...")
            UdpFileHandler.beg = time.time()

        elif msg == b'1':
            print(time.time()-UdpFileHandler.beg, UdpFileHandler.totals)
            print("over")

        else:
            UdpFileHandler.totals += len(msg)


def recv_by_udp():
    with UDPServer(('', 8080), UdpFileHandler) as serv:
        serv.max_packet_size = 64*1024
        serv.serve_forever()

if __name__ == "__main__":
    recv_by_udp()
