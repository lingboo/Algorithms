n = input().strip()
def cal_len(num):
    ans = 0
    while num:
        ans += 1
        num /= 10
    return ans
squares = set()
for i in range(1, 100000+1):
    squares.add(i**2)
len_ = -1
for i in range(1 << len(n)):
    first = -1
    num = 0
    for j in range(len(n)):
        if i & (1 << j):
            if first == -1 and n[j] == "0":
                break
            else:
                first = j
                num = num * 10 + (int(n[j]) - 0)
    if num in squares:
        len_ = max(len_, cal_len(num))
if len_ == -1:
    print("-1")
else:
    print(len(n) - len_)