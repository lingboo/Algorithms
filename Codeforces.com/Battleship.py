n, k = map(int, input().split())
graph = [[0]*n for __ in range(n)]
for i in range(n):
    r = input().strip()
    for c in range(len(r)):
        if r[c] == ".":
            graph[i][c] = 1
row = 0
max_row = 0
max_column = 0
column = 0
for g in range(n):
    temp = 0
    count = 0
    for i in range(n):
        if graph[g][i] == 1:
            count += 1
        else:
            count = 0
        temp = max(count, temp)
    if max_row < temp:
        max_row = temp
        row = g
for g in range(n):
    count = 0
    temp = 0
    for i in range(n):
        if graph[i][g] == 1:
            count += 1
        else:
            count = 0
        temp = max(temp, count)
    if max_column < temp:
        max_column = temp
        column = g
print(str(row+1) + " " + str(column+1))
