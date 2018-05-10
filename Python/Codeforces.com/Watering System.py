n, A, B = map(int, input().split())
s = list(map(int, input().split()))
first = s[0]
s = s[1:]
s.sort(reverse=True)
sum_ = sum(s) + first
i = 0
res = 0
while (A*first)/sum_ < B:
    sum_ -= s[i]
    res += 1
    i += 1
print(res)