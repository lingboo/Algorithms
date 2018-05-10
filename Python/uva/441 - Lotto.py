inputs = []
while True:
    arr = list(map(int, input().split()))
    if len(arr) == 1:
        break
    inputs.append(arr)

for i in inputs:
    k = i[0]
    i = i[1:]
    for a in range(k-5):
        for b in range(a+1, k-4):
            for c in range(b+1, k-3):
                for d in range(c+1, k-2):
                    for e in range(d+1, k-1):
                        for f in range(e+1, k):
                            print("%d %d %d %d %d %d" % (i[a], i[b], i[c], i[d], i[e], i[f]))
    if i != inputs[-1][1:]:
        print()