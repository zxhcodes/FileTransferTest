import time

totals = 0

beg = time.time()

with open("/rsdata/bigfile.bin", "rb") as r:
    while True:
        chunk = r.read(1024*1024)
        if not chunk:
            break
        totals += len(chunk)

print(time.time()-beg, totals)