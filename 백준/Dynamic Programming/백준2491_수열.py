n = int(input())
num = list(map(int, input().split()))
rise = [1]*n
fall = [1]*n
for i in range(1, n):
    if num[i-1] <= num[i]:
        rise[i] = rise[i-1] + 1
    if num[i-1] >= num[i]:
        fall[i] = fall[i-1] + 1
print(max(max(rise), max(fall)))
