if __name__ == '__main__':
    t = int(input().strip())
    for c in range(1, t+1):
        n = int(input().strip())
        done = False
        ants = list(map(int, input().split()))
        res = 1
        strength = [a*6 for a in ants]
        k = n
        for i in range(n-1, -1, -1):
            if i == k - 1:
                continue
            for j in range(i+1, k):
                strength[j] -= ants[i]
                if strength[j] < 0:
                    done = True
                    k = j + 1
                    break
            if not done:
                res += 1
            else:
                done = False

        print("Case #%d:  %d" % (c, res))


