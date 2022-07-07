#첫 번째 풀이
def solution(n, arr1, arr2):
    answer = [""]*n
    for i in range(n):
        for j in range(n):
            if arr1[i]%2 == 0 and arr2[i]%2 == 0:
                answer[i] = " " + str(answer[i])
            else:
                answer[i] = "#" + str(answer[i])
            arr1[i] = arr1[i]//2
            arr2[i] = arr2[i]//2
    return answer


#두 번째 풀이

def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        num = str(bin(i|j))[2:]
        num = num.rjust(n,"0")
        num = num.replace("0"," ")
        num = num.replace("1","#")
        answer.append(num)
    return answer
