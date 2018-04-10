n = int(input().strip())
points = []
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

first = points[0]
second = points[1]
