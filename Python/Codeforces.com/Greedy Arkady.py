n, k, M, D = map(int, input().split())
ans = 0
for d in range(1, D+1):
    x = min(n//((d-1)*k + 1), M)
    if x > M:
        continue
    ans = max(d*x, ans)
print(ans)