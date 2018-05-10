if __name__ == '__main__':
    T = int(input().strip())
    for _ in range(T):
        n = int(input().strip())
        a = list(map(int, input().split()))
        b = [0]*n
        for i in range(1, n):
            temp = 0
            for j in range(i):
                if a[i] >= a[j]:
                    temp += 1
            b[i] = temp
        print(sum(b))