arr = list(map(int, input().split()))
res = 0
for i in range(14):
    temp_arr = arr.copy()
    current = temp_arr[i]
    temp_arr[i] = 0
    d = current//14
    mod = current % 14
    for t_ in range(14):
        temp_arr[t_] += d
    for t in range(1, mod + 1):
        temp_arr[(t+i) % 14] += 1
    count = 0
    for ta in temp_arr:
        if ta % 2 == 0:
            count += ta
    res = max(res, count)
print(res)