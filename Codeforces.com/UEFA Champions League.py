import sys
T = int(input().strip())
arr_inputs = list(sys.stdin.readline() for _ in range(T))

for inp in arr_inputs:
    a, b, c, d = map(int, inp.split())
    first = a + c
    second = b + d
    if first == second:
        if b < c:
            print(1)
        elif b > c:
            print(2)
        else:
            print(-1)
    elif first > second:
        print(1)
    else:
        print(2)

