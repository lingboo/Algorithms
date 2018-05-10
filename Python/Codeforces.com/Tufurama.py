n = int(input().strip())
a = list(map(int, input().split()))
for i in range(n):
    a[i] = min(a[i], n)
print(a)