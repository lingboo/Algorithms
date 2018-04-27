import sys
t = int(input().strip())
for _ in range(t):
    paid = {}
    total_amount = 0
    k = int(input().strip())
    for __ in range(k):
        ch, money = map(str, input().split())
        paid.setdefault(ch, int(money))
    m = int(input().strip())
    lines = [sys.stdin.readline() for ___ in range(m)]
    for l in lines:
        for ch in l:
            if paid.get(ch) is not None:
                total_amount += paid[ch]
    total_amount /= 100
    print(str(total_amount)+"$")