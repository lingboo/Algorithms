t = int(input().strip())
for _ in range(t):
    arr = list(map(int, input().split()))
    n = arr[0]
    arr = arr[1:]
    print("Case "+str(_+1)+": "+str(max(arr)))