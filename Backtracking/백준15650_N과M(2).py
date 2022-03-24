n, m = map(int, input().split())
result = []

def func(start):
    if len(result) == m:
        for i in result:
            print(i, end = ' ')
        print()
        return
    for i in range(start, n+1):       
        if i not in result:
            result.append(i)
            func(i+1)
            result.pop()
func(1)
