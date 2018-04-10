def reduce(numerator, denominator):
    for i in range(2, numerator+1):
        if numerator % i == 0 and denominator % i == 0:
            return reduce(numerator // i, denominator // i)
    return numerator, denominator
y, w = map(int, input().split())
max_ = max(y, w)
a, b = reduce(6-max_ + 1, 6)
print(str(a)+"/"+str(b))
