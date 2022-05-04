N, M = map(int, input().split())
result = []

def func():
    if len(result) == M:
        for i in result:
            print(i, sep=' ')
        return
    for i in range(1, N+1):
        if i not in result:
            result.append(i)
            func()
            result.pop()
func()
