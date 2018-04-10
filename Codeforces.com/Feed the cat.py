import math as m
hh, mm = map(int, input().split())
H, D, C, N = map(int, input().split())
if hh >= 20:
    at_current = float(0.8*C * m.ceil(H / N))
    res = at_current
else:
    minutes = (20 - hh)*60 + 00 - mm
    at_current = float(C * m.ceil(H / N))
    at_20 = float(m.ceil((H+D*minutes)/N)*(C*0.8))
    res = min(at_current, at_20)
print("{0:.4f}".format(res))