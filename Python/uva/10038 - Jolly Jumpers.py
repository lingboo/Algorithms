while True:
    try:
        arr = list(map(int, input().split()))
        n = arr[0]
        check = [False]*(n-1)
        i = 1
        count = 0
        if n == 1:
            count += 1
        else:
            while i < n:
                if 1 <= abs(arr[i]-arr[i+1]) < n and not check[abs(arr[i] - arr[i+1])-1]:
                    check[abs(arr[i] - arr[i+1])-1] = True
                    count += 1
                i += 1
        if count >= n - 1:
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        exit(0)
        break
