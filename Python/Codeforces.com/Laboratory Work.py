n = int(input().strip())
arr = list(map(int, input().split()))
a = arr.count(min(arr))
c = arr.count(max(arr))

b = n - (a + c)
print(b)