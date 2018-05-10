t = int(input().strip())
for _ in range(t):
    n, k = map(int, input().split())
    print(k ^ (k >> 1))