import math as m
k, n, s, p = map(int, input().split())
needed_sheets = k * m.ceil(n/s)
res = m.ceil(needed_sheets/p)
print(res)