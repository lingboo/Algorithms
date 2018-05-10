# http://acm.timus.ru/problem.aspx?space=1&num=1020
import math as m

n, r = map(float, input().split())
n = int(n)
coordinates = []
for _ in range(n):
    coordinates.append(list(map(float, input().split())))

length = 0.0
for index in range(n):
    if index == n - 1:
        length += m.sqrt((coordinates[index][0]-coordinates[0][0])**2 + (coordinates[index][1]-coordinates[0][1])**2)
    else:
        length += m.sqrt((coordinates[index][0]-coordinates[index+1][0])**2 + (coordinates[index][1]-coordinates[index+1][1])**2)

print("{0:.2f}".format(length+2*m.pi*r))
