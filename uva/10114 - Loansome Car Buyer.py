while True:
    arr = list(map(float, input().split()))
    if arr[0] < 0:
        break
    depreciations = {}
    payment_down = arr[2]
    for _ in range(int(arr[3])):
        m, a = map(float, input().split())
        depreciations.setdefault(int(m), a)
    current_value = arr[2] - arr[2]*depreciations[0]
    temp = 0
    for i in range(1, int(arr[0])):
        payment_down -= arr[1]
        if depreciations.get(i) is not None:
            temp = i
        current_value = current_value - current_value*depreciations[temp]
        if payment_down < current_value:
            break
    print(i)