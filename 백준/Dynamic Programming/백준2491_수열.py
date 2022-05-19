n = int(input())
nums = list(map(int, input().split()))
result = 1

rise = [1] * n
fall = [1] * n

for i in range(1, n):
    if nums[i-1] <= nums[i]:
        rise[i] = rise[i-1] + 1
    if nums[i-1] >= nums[i]:
        fall[i] = fall[i-1] + 1

print(max(max(rise), max(fall)))
