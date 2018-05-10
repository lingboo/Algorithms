n = int(input().strip())
s = input().strip()
flag = False
temp = ""
for i in range(n):
    if s[i] == "0":
        temp += s[i]
    elif not flag and s[i] == "1":
        flag = True
        temp = s[i]+temp
print(temp)


