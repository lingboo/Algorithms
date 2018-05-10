n, k = map(int, input().split())
theorems = list(map(int, input().split()))
sleep = list(map(int, input().split()))
max_ = 0
res = 0
sum_ = 0
for i in range(n):
    if sleep[i] == 1:
        res += theorems[i]
        theorems[i] = 0
    sum_ += theorems[i]
    j = i - k
    if j >= 0:
        sum_ -= theorems[j]
    max_ = max(max_, sum_)
print(res+max_)