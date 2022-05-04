# x + Mm = y + Nn이다. (m, n은 각각 M, N을 더한 횟수)
# 이때 (y + Nn)%N = y 인데, 위의 식에 따라 대입하면 (x + Mm)%N = y도 성립한다.
# 이는 곧 ((x+Mm)-y)%N = 0을 의미한다.

def year(M, N, x, y):
    while x <= M * N:
        if (x-y)%N == 0:
            return x
        x += M
    return -1
    
T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    print(year(M, N, x, y))
    
