n, m = map(int, input().split())
result = []
def func(start):
    if len(result) == m:
        for i in result:
            print(i, end=' ')
        print()
        return
    for i in range(start, n+1):
        result.append(i)
        func(i)
        result.pop()
func(1)
