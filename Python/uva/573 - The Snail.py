while True:
    h, u, d, f = map(int, input().split())
    if h == 0:
        break
    init = 0
    days = 0
    distance_reduce = u
    done = ""
    while init < h:
        days += 1
        if distance_reduce > 0:
            init += distance_reduce
        if init > h:
            done = "success"
            break
        init -= d
        if init < 0:
            done = "failure"
            break
        distance_reduce -= u*(f/100)
    print(done+" on day "+str(days))