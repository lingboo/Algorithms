n = int(input().strip())
arr_s = list(map(str, input().split()))
res = 0
checked = []
for s in arr_s:
    temp = ""
    words = [0]*26
    for ch in s:
        if temp.find(ch) == -1:
            temp += ch
            words[ord(ch) - 97] += 1
    if len(checked) == 0:
        checked.append(words)
        res += 1
    else:
        try:
            checked.index(words)
        except ValueError:
            checked.append(words)
            res += 1
print(res)