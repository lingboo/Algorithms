while True:
    try:
        n, b, h, w = map(int, input().split())
        cost = 500001
        for i in range(h):
            price = int(input().strip())
            beds = list(map(int, input().split()))
            for bed in beds:
                if bed >= n:
                    cost = min(cost, price*n)
        if cost > b:
            print("stay home")
        else:
            print(cost)
    except EOFError:
        exit(0)