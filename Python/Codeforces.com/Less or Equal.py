n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = -1
if k == 0 and arr[0] != 1:
    res = 1
elif k == 1:
    res = min(arr[0], 10**9)
else:
    for i in range(n-1):
        if i == k - 1 and arr[i] != arr[i+1]:
            res = arr[i] + 1
print(res)
