import sys
n, s = map(int, input().split())
inputs = [sys.stdin.readline() for _ in range(n)]
init = 0
checked = False
last = False
res = [0, 0]
for i in inputs:
    h, m = map(int, i.split())
    current = h*60 + m
    if not checked and init == 0 and init + s + 1 <= current:
        break
    if init + 2*s + 2 <= current:
        a = (init + s + 1) // 60
        b = (init + s + 1) % 60
        res = [a, b]
        break
    else:
        init = current
        if init == 0:
            checked = True
    if i == inputs[-1]:
        last = True
if last:
    h, m = map(int, inputs[-1].split())
    minutes = h*60 + m + s + 1
    a = minutes // 60
    b = minutes % 60
    res = [a, b]
print(str(res[0])+" "+str(res[1]))

