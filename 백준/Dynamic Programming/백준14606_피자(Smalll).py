N = int(input())
result = 0
def devide(N):
    global result
    if(N == 1): return
    if N % 2 == 0: #even
        n1 = N / 2
        n2 = N / 2
        result += n1 * n2
        devide(n1)
        devide(n2)
    else: #odd
        n1 = int(N / 2)
        n2 = N - n1
        result += n1 * n2
        devide(n1)
        devide(n2)

devide(N)
print(int(result))
