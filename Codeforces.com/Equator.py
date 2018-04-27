n = int(input().strip())
arr = list(map(int, input().split()))
sum_ = sum(arr)/2
temp = 0
res = 0
for i in range(n):
    temp += arr[i]
    if temp >= sum_:
        res = i + 1
        break
print(res)