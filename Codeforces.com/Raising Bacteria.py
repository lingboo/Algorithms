x = int(input().strip())
base = 1
count = 1
while base < x:
    base <<= 1
    if base > x:
        x -= (base >> 1)
        base = 1
        count += 1
print(count)
