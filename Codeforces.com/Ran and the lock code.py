import sys
T = int(input().strip())
arr_inputs = list(sys.stdin.readline().strip() for _ in range(T))

MIN = 1
MAX = 10**9
MAX_LIST = MAX / 2
for i in arr_inputs:
    res = 0
    n, a = map(int, i.split())
    if a <= MAX_LIST:
        res = min((a - MIN)*2 + 1, n)
    else:
        res = min((MAX - a)*2 + 1, n)
    print(res)


