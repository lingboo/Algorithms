n, m, k = map(int, input().split())
if k < n:
    print("%d %d" % (k + 1, 1))
else:
    row = n - (k - n) // (m-1)
    if row & 1:
        print("%d %d" % (row, m - (k - n) % (m - 1)))
    else:
        print("%d %d" % (row, (k - n) % (m - 1) + 2))
