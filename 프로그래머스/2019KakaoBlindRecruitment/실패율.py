def solution(N, stages):
    answer = {}
    lens = len(stages)
    for stage in range(1,N+1):
        tmp = stages.count(stage)
        if tmp != 0:
            answer[stage] = stages.count(stage) / lens
            lens -= tmp
        else:
            answer[stage] = 0
    answer = sorted(answer, key = lambda x: answer[x], reverse = True)
    return answer
