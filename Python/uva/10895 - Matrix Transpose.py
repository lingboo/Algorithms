while True:
    try:
        n, m = map(int, input().split())
        transpose_matrix = [[0]*n for _ in range(m)]
        for r in range(n):
            indices = list(map(int, input().split()))
            c = indices[0]
            if c == 0:
                input()
                continue
            values = list(map(int, input().split()))
            for i in range(1, c+1):
                transpose_matrix[indices[i]-1][r] = values[i-1]

        res_size = "%d %d" % (m, n)
        print(res_size)
        for r in range(m):
            res_indices = ""
            res_values = ""
            count = 0
            for c in range(n):
                if transpose_matrix[r][c] != 0:
                    count += 1
                    res_indices += str(c+1) + " "
                    res_values += str(transpose_matrix[r][c])+" "
            print((str(count)+" "+res_indices.strip()).strip())
            print(res_values.strip())
    except EOFError:
        exit(0)
        break

