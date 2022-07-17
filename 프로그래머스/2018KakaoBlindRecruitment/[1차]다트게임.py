def solution(dartResult):
    answer = 0
    nums = []
    j = -1
    dartResult = dartResult.replace('10', 'x')
    for i in dartResult:
        if i.isnumeric() == True:
            nums.append(int(i))
            j += 1
        elif i == 'x':
            nums.append(10)
            j += 1
        elif i == 'D':
            nums[j] = pow(nums[j], 2)
        elif i == 'T':
            nums[j] = pow(nums[j], 3)
        elif i == "*":
            nums[j] = nums[j] * 2
            if j > 0:
                nums[j-1] = nums[j-1] * 2
        elif i == "#":
            nums[j] *= -1
    answer = sum(nums)
    return answer
