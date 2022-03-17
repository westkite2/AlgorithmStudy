target = int(input())
answer = abs(target-100)
brokenTotal = int(input())

if brokenTotal:
    broken = set(input().split())
else:
    broken = set()

for num in range(1000001):
    snum = str(num)
    for j in range(len(snum)):
        if snum[j] in broken:
            break
        elif j == len(snum) - 1:
            answer = min(answer, len(snum) + abs(target-num))
print(answer)
