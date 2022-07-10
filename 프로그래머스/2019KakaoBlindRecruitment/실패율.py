def solution(N, stages):
    answer = {}
    users = len(stages)

    for i in range(1, N+1):
        stay = stages.count(i)
        if stay != 0:
            answer[i] = stay/users 
            users -= stay
        else:
            answer[i] = 0
    answer = sorted(answer, key = lambda i : answer[i], reverse = True)
    return answer
