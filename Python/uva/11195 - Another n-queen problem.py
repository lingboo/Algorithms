import sys

def backtrack(c):
    global ans, rw, ld, rd
    if c == n:
        ans += 1
        print(ans)
        return
    for r in range(n):
        if board[r][c] != "*" and not rw[r] and not ld[r - c + n - 1] and not rd[r + c]:
            rw[r] = ld[r - c + n - 1] = rd[r + c] = True
            backtrack(c + 1)
            rw[r] = ld[r - c + n - 1] = rd[r + c] = False
if __name__ == '__main__':
    case = 1
    while True:
        n = int(input().strip())
        if n == 0:
            break
        board = [sys.stdin.readline().strip() for _ in range(n)]
        ld, rd = ([False] * (2*n -1),)*2
        rw = [False]*n
        ans = 0
        backtrack(0)
        print("Case %d: %d" % (case, ans))
        case += 1