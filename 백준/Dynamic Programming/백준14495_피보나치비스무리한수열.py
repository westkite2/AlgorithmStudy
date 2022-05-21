n = int(input())
result = 0
x, y, z = 1, 1, 1
for i in range(4, n+1):
    x, y, z = y, z, x+z 
result = z
print(result)
