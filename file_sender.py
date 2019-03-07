import io
from socket import socket, AF_INET, SOCK_STREAM, SOCK_DGRAM

files = ["LC80100052018170LGN00.tgz", "LC80100032018170LGN00.tgz", "LC80062352018174LGN00.tgz"]

mem = io.BytesIO()

for f in files[:1]:
    with open("/tmp/landsat8/"+f, "rb") as lc:
        mem.write(lc.read())


def send_by_tcp():
    tcp_sock = socket(AF_INET, SOCK_STREAM)
    tcp_sock.connect(("10.0.86.121", 8080))
    tcp_sock.send(mem.getvalue())
    tcp_sock.close()


def send_by_udp():
    udp_sock = socket(AF_INET, SOCK_DGRAM)

    udp_sock.sendto(b'0', ('10.0.86.121', 8080))
    mem.seek(0)
    totals, idx = 0, 0
    while True:
        chunk = mem.read(32*1024)
        if not chunk:
            break
        num = udp_sock.sendto(chunk, ('10.0.86.121', 8080))
        totals += num

    udp_sock.sendto(b'1', ('10.0.86.121', 8080))

    print(totals)


if __name__ == '__main__':
    send_by_udp()

