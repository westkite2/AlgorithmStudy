def isPrime(num):
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

def solution(nums):
    answer = 0
    sum = 0
    numslen = len(nums)
    for i in range(0, numslen-2):
        for j in range(i+1, numslen-1):
            for k in range(j+1, numslen):
                if(isPrime(nums[i]+nums[j]+nums[k])):
                    answer += 1

    return answer
