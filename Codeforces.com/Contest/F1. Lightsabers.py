
n, m = map(int, input().split())
lightsabers = list(map(int, input().split()))
colors = list(map(int, input().split()))
done = False
for i in range(n-m+1):
    count = 0
    visited = [False] * m
    j = i
    interval = j + m
    while j < interval:
        if not visited[lightsabers[j]-1]:
            visited[lightsabers[j]-1] = True
            count += 1
        j += 1
    if count == m:
        done = True
        break
if done:
    print("YES")
else:
    print("NO")