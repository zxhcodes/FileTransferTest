import io
from socket import socket, SOCK_STREAM, AF_UNIX, AF_INET

mem = io.BytesIO()

with open("/rsdata/bigfile.bin", "rb") as lc:
    mem.write(lc.read())


def send_by_unix():
    unix_sock = socket(AF_UNIX, SOCK_STREAM)
    unix_sock.connect("/tmp/unix_1.sock")
    print("start sending...")
    unix_sock.send(mem.getvalue())
    unix_sock.close()
    print("over!")

def send_by_tcp():
    unix_sock = socket(AF_INET, SOCK_STREAM)
    unix_sock.connect(("xx.xx.xx.xx", 8080))
    print("start sending...")
    unix_sock.send(mem.getvalue())
    unix_sock.close()
    print("over!")


if __name__ == '__main__':
    send_by_tcp()
