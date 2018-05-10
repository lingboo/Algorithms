n = int(input().strip())
s = input().strip()
mapped = dict()
for i in range(n - 1):
    if s[i]+s[i+1] not in mapped:
        mapped[s[i]+s[i+1]] = 1
    else:
        mapped[s[i]+s[i+1]] += 1

max_ = 0
res = ""
for k in mapped:
    if max_ < mapped[k]:
        max_ = mapped[k]
        res = k
print(res)