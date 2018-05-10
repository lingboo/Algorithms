t = int(input().strip())
for _ in range(1, t+1):
    a = list(map(int, input().split()))
    a.sort()
    print("Case "+str(_)+": "+str(a[1]))