N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[float('inf')]*3 for _ in range(M)] for _ in range(N)]

for y in range(N):
    if y == 0: #첫 행
        for x in range(M):
            for d in range(3):
                dp[y][x][d] = board[y][x]
    else:
        for x in range(M):
            if x == 0: #왼쪽 열
                dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2]) + board[y][x]
                dp[y][x][1] = dp[y-1][x][2] + board[y][x]
            elif x == M-1: #오른쪽 열
                dp[y][x][1] = dp[y-1][x][0] + board[y][x]
                dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + board[y][x]
            else:
                dp[y][x][0] = min(dp[y-1][x+1][1], dp[y-1][x+1][2])+ board[y][x]
                dp[y][x][1] = min(dp[y-1][x][0], dp[y-1][x][2]) + board[y][x]
                dp[y][x][2] = min(dp[y-1][x-1][0], dp[y-1][x-1][1]) + board[y][x]
                

#마지막 행
result = float('inf')
for x in range(M):
        result = min(min(dp[N-1][x]), result)
print(result)
