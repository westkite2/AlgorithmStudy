def checkboard(board, n):
    maxcnt = 1
    for i in range(n):
        cnt = 1
        for j in range(n-1):
            if board[i][j] == board[i][j+1]:
                cnt += 1
            else:
                cnt = 1
            if maxcnt < cnt:
                maxcnt = cnt
        cnt = 1
        for j in range(n-1):            
            if board[j][i] == board[j+1][i]:
                cnt += 1
            else:
                cnt = 1
            if maxcnt < cnt:
                maxcnt = cnt
    return maxcnt

n = int(input())
board = [list(input()) for _ in range(n)]
answer = 0

for i in range(n):
    for j in range(n):
        if j < n-1:
            tmpvar = board[i][j]
            board[i][j] = board[i][j+1]
            board[i][j+1] = tmpvar
            tmp = checkboard(board, n)
            if answer < tmp:
                answer = tmp
            tmpvar = board[i][j]
            board[i][j] = board[i][j+1]
            board[i][j+1] = tmpvar
            
        if i < n-1:
            tmpvar = board[i][j]
            board[i][j] = board[i+1][j]
            board[i+1][j] = tmpvar
            tmp = checkboard(board, n)
            if answer < tmp:
                answer = tmp
            tmpvar = board[i][j]
            board[i][j] = board[i+1][j]
            board[i+1][j] = tmpvar
print(answer)
