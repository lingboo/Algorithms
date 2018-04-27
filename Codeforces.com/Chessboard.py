import sys
n = int(input().strip())
count = 0
if n == 1:
    ones = 0
    zeros = 0
    for _ in range(4):
        a = int(input().strip())
        input() if _ < 3 else None
        ones = ones + 1 if a == 1 else ones
        zeros = zeros + 1 if a == 0 else zeros
    ones >>= 1
    zeros >>= 1
    count = abs(ones - zeros)
else:
    chess_board = [[] for i in range(4)]
    for _ in range(4):
        piece = [int(sys.stdin.readline(), 2) for _ in range(n)]
        input() if _ < 3 else None
        if (1 << n - 1) & (piece[0] & (1 << n - 1)):
            if len(chess_board[0]) == 0:
                chess_board[0] = piece
            else:
                chess_board[2] = piece
        else:
            if len(chess_board[1]) == 0:
                chess_board[1] = piece
            else:
                chess_board[3] = piece
    for p in range(4):
        if p % 2 == 0:
            for i in range(n):
                if i % 2 == 0:
                    for j in range(0, n, 2):
                        if not chess_board[p][i] & (1 << j):
                            count += 1
                        if chess_board[p][i] & ((1 << j) >> 1) and j > 0:
                            count += 1
                else:
                    for j in range(0, n, 2):
                        if chess_board[p][i] & (1 << j):
                            count += 1
                        if not chess_board[p][i] & ((1 << j) >> 1) and j > 0:
                            count += 1
        else:
            for i in range(n):
                if i % 2 == 0:
                    for j in range(0, n, 2):
                        if chess_board[p][i] & (1 << j):
                            count += 1
                        if not chess_board[p][i] & ((1 << j) >> 1) and j > 0:
                            count += 1
                else:
                    for j in range(0, n, 2):
                        if not chess_board[p][i] & (1 << j):
                            count += 1
                        if chess_board[p][i] & ((1 << j) >> 1) and j > 0:
                            count += 1

print(count)