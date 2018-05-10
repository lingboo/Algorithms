n = int(input().strip())
potencies = [0]*(1 << 15)
m = 0
for i in range(1 << n):
    w = int(input().strip())
    for j in range(1 << n):
        if i != j:
            n = i ^ j
            if n & -n == n:
                potencies[j] += w
for i in range(1 << n):
    for j in range(j << n):
        if i == j or (i ^ j) & -(i ^ j) != (i ^ j):
            continue
        m = max(m, potencies[i]+potencies[j])
print(m)