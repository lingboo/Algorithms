n, k, M, D = map(int, input().split())
ans = 0
for d in range(1, D+1):
    x = n//k if d == 1 else n//((d*k) - (k-1))
    max_ = min(x, M)
    ans = max(d*max_, ans)
print(ans)