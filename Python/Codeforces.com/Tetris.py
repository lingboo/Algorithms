n, m = map(int, input().split())
count = [0]*(n+1)
columns = list(map(int, input().split()))
for c in columns:
    count[c] += 1
min_ = 1000
for i in range(1, n+1):
    min_ = min(min_, count[i])
print(min_)