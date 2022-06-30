R, C = map(int, input().split())
board = [list(input()) for _ in range(R)]
result = 2500
for r in range(R-7):
    for c in range(C-7):
        white, black = 0, 0
        for i in range(r, r+8):
            for j in range(c, c+8):
                if (i+j)%2 == 0:
                    if board[i][j] != 'W': white += 1
                    if board[i][j] != 'B': black += 1
                else:
                    if board[i][j] != 'B': white += 1
                    if board[i][j] != 'W': black += 1
        result = min(result, min(white, black))
print(result)
