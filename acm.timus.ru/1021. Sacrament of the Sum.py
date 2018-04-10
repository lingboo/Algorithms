list_a = []
n = int(input().strip())
for _ in range(n):
    list_a.append(int(input().strip()))
m = int(input().strip())
list_b = []
for _ in range(m):
    list_b.append(int(input().strip()))
a = ()
i = 0
j = 0
done = False
while i < n:
    while j < m:
        if i >= n:
            break
        if list_a[i] + list_b[j] < 10000:
            i += 1
        elif list_a[i] + list_b[j] > 10000:
            j += 1
        else:
            done = True
            break
    if done or j >= m:
        break
    a.count()

if done:
    print("YES")
else:
    print("NO")
