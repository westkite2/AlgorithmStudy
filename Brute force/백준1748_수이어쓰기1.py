N = input()
nlen = len(N)
sum = 0
for i in range(nlen - 1):
    sum += 9 * (10**i) * (i+1)
sum += (int(N) - (10**(nlen-1)) + 1) * nlen
print(sum)
