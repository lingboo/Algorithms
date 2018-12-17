def sum_in_grid(grid):
    m = len(grid)
    n = len(grid[0])
    sum = [[0]*n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                sum[i][j] = grid[i][j]
            elif i == 0 and j != 0:
                sum[i][j] = sum[i][j-1] + grid[i][j]
            elif i != 0 and j == 0:
                sum[i][j] = sum[i-1][j] + grid[i][j]
            else:
                sum[i][j] = max(sum[i-1][j], sum[i][j-1]) + grid[i][j]
    return sum

def path_in_grid(sum):
    i = len(sum)-1
    j = len(sum[0])-1
    path = [(i, j)]
    while i > 0 or j > 0:
        if sum[i-1][j] > sum[i][j-1]:
            path.append((i-1,j))
            i -= 1
        else:
            path.append((i, j-1))
            j -= 1
    return path

grid = [[3,7,9,2,7],[9,8,3,5,5],[1,7,9,8,5],[3,8,6,4,10],[6,3,9,7,8]]
res = sum_in_grid(grid)
