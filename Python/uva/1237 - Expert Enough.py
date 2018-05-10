import sys
if __name__ == '__main__':
    T = int(input().strip())
    line = 1
    for _ in range(T):
        D = int(input().strip())
        mapped = {}
        for __ in range(D):
            M, L, H = map(str, input().split())
            mapped[M] = (int(L), int(H))
        Q = int(input().strip())
        query = [int(sys.stdin.readline()) for ___ in range(Q)]
        for q in query:
            count = 0
            res = "UNDETERMINED"
            for k in mapped.keys():
                a = mapped[k][0]
                b = mapped[k][1]
                if a <= q <= b:
                    res = k
                    count += 1
                if count > 1:
                    res = "UNDETERMINED"
                    break
            print(res)
        if _ < T - 1:
            print()
