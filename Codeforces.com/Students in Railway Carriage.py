n, a, b = map(int, input().split())
string = input().strip()
arr = string.split("*")
len_ = [len(i) for i in arr]
total = a + b
for nums in len_:
    temp1 = nums >> 1
    temp2 = nums - temp1
    if a <= b:
        a -= temp1
        b -= temp2
    else:
        a -= temp2
        b -= temp1
a = max(0, a)
b = max(0, b)
print(total - a - b)