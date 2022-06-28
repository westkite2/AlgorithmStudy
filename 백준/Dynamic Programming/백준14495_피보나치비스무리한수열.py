n = int(input())
a,b,c=1,1,1
for _ in range(n-3):
    a,b,c=b,c,a+c
result = c
print(result)
