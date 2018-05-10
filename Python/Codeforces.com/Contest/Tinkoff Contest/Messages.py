n, A, B, C, T = map(int, input().split())
arr = list(map(int, input().split()))
res = 0
if B >= C:
    res = n*A
else:
    for a in arr:
        res += (A + (T - a))
print(res)