m = int(input().strip())
coordinates = []
for _ in range(m):
    e = input().strip()
    nums = []
    i = 0
    while i < len(e):
        num = ""
        if e[i].isdigit():
            while i < len(e) and e[i].isdigit():
                num += e[i]
                i += 1
            nums.append(int(num))
        else:
            i += 1
    c = (nums[0] + nums[1]) / nums[2]
    coordinates.append(c)
res = ""
for co in coordinates:
    res += str(coordinates.count(co))+" "
print(res.strip())