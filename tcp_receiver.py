import time
from socketserver import BaseRequestHandler, UnixStreamServer, TCPServer


class FileReceiver(BaseRequestHandler):
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

def recv_by_unix():
    with UnixStreamServer("/tmp/unix_1.sock", FileReceiver) as serv:
        serv.serve_forever()

def recv_by_tcp():
    with TCPServer(("xx.xx.xx.xx", 8080), FileReceiver) as serv:
        serv.serve_forever()

if __name__ == "__main__":
    recv_by_tcp()
