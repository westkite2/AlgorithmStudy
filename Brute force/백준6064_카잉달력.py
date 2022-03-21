#시간초과
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    cx, cy, result = 1, 1, 1
    while True:
        if cx == x and cy == y:            
            break
        if cx == M and cy == N:
            result = -1
            break
        cx += 1
        cy += 1
        result += 1
        if cx > M:
            cx = 1
        if cy > N:
            cy = 1
    print(result)
