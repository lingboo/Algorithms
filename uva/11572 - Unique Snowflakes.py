import sys
t = int(input().strip())
for _ in range(t):
    unique = dict()
    n = int(input().strip())
    for __ in range(n):
        a = int(sys.stdin.readline())
        if a not in unique:
            unique.setdefault(a, 1)
        else:
            unique[a] += 1
    print(unique)