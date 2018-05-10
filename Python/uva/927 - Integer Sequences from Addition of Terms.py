def findn(d, k):
    p = 0
    n = 1
    while True:
        previous = p
        p += n*d
        if previous < k <= p:
            return n
        n += 1

if __name__ == '__main__':
    t = int(input().strip())
    for _ in range(t):
        sequence = list(map(int, input().split()))
        d = int(input().strip())
        k = int(input().strip())
        n = findn(d, k)
        for i in range(len(sequence)):
            sequence[i] *= n**i
        print(sequence)

