n = int(input().strip())
chess_board = []
for _ in range(4):
    piece = []
    for row in range(n):
        piece.append(row)
    chess_board.append(piece)
    input()