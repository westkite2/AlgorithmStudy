T = int(input())

def getsum(n):
    #f(n) = f(n-1) + f(n-2) + f(n-3)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return getsum(n-1) + getsum(n-2) + getsum(n-3)
    
for _ in range(T):
    num = int(input())
    print(getsum(num))
