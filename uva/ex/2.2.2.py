S = int(input().strip())
n = len("{0:b}".format(S))
res3 = 0
res4 = 0
for i in range(n):
    if S & (1 << i):
        res3 = S & ~(1 << i)
        break
for i in range(n):
    if not S & (1 << i):
        res4 = S ^ (1 << i)
        break
print(res3)
print(res4)
if S & -S == S:
    print("YES")
else:
    print("NO")

res5 = 0
for i in range(n):
    if S & (1 << i):
        continue
    else:
        res5 = S ^ (1 << i)-1
        break
print(res5)
res6 = 0
for i in range(n):
    if not S & (1 << i):
        continue
    else:
        res6 = S ^ (1 << i)-1
        break
print(res6)
