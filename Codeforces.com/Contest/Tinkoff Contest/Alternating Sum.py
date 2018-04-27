n, a, b, k = map(int, input().split())
sequence = input().strip()
res = 0
sign = 0
for i in range(n+1):
    if i < k:
        if sequence[i] == "+":
            sign = 1
        else:
            sign = -1
    res += sign*(a**(n - i) * b**i)
print(res % (10**9 + 9))