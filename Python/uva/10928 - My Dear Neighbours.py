t = int(input().strip())
for _ in range(t):
    n = int(input().strip())
    neighbor = []
    min_ = 10**5
    for __ in range(n):
        arr = list(map(int, input().split()))
        neighbor.append(len(arr))
        min_ = min(min_, len(arr))
    if _ < t - 1:
        input()
    res = ""
    for i in range(len(neighbor)):
        if neighbor[i] == min_:
            res += str(i+1)+" "
    print(res.strip())