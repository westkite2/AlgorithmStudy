n=int(input())
result = 0

def parsing(h, t, o):
    if h-t == t - o: return 1
    else: return 0
    
for i in range(1, n+1):
    if i<100: result += 1
    elif i<1000: result += parsing(i//100, (i%100)//10, (i%100)%10)

print(result)

#numlist = list(map(int, str(i)))
#numlist[0]-numlist[1] = numlist[1] - numlist[2]
