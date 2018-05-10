if __name__ == '__main__':
    try:
        while True:
            result = []
            k = int(input().strip())
            count = 0
            for y in range(k+1, 2*k + 1):
                a = k * y
                b = y - k
                c = a % b
                if (k * y) % (y - k) == 0:
                    result.append(((k*y)//(y-k), y))
                    count += 1
            print(count)
            for i in result:
                print("1/%d = 1/%d + 1/%d" % (k, i[0], i[1]))
    except EOFError:
        exit(0)