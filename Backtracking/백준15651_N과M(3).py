n, m = map(int, input().split())
result = []

def func(j):
    if j == m:
        for k in result:
            print(k, end = ' ')
        print()
        return
    j += 1
    for i in range(1, n+1):
        result.append(i)
        func(j)
        result.pop()
func(0)
