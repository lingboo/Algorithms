import sys
n, m, k = map(int, input().split())
a = [int(sys.stdin.readline()) for _ in range(m+1)]
fedor = a[-1]
count = 0
for i in range(m):
    b = "{0:b}".format(a[i] ^ fedor)
    g = 0
    for c in b:
        if c == "1":
            g += 1
    if g <= k:
        count += 1
print(count)