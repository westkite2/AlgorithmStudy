N = int(input())
num = list(map(int, input().split()))

for i in range(N-1, 0, -1):
    if num[i] < num[i-1]:
        if i == 1:
            print(-1)
            break
        else:
            continue
    else:
        for j in range(N-1, i-1, -1):        
            if num[j] > num[i-1]:
                num[j], num[i-1] = num[i-1], num[j]                
                num = num[:i] + sorted(num[i:N])
                print(*num)
                break
        break
