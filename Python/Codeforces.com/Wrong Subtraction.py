n, k = map(int, input().split())
while n:
    a = n % 10
    if k <= a or k == 0:
        n -= k
        break
    k -= a
    n //= 10
    k -= 1


print(n)