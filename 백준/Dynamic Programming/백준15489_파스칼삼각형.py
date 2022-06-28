matrix = [[1 for _ in range(30)] for _ in range(30)]

def pascal(matrix):
    for i in range(30):
        for j in range(1, 30):
            if j==i: matrix[i][j] = 1
            else: matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]

r,c,w = map(int, input().split())
pascal(matrix)
result = 0
cnt = 1
for i in range(r-1, r+w-1):
    for j in range(cnt):
        result += matrix[i][c-1+j]
    cnt += 1
        
print(result)
