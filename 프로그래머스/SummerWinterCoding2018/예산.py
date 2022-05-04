def solution(d, budget):
    answer = 0
    d.sort()
    dlen = len(d)
    i = 0
    sum = 0
    while(i < dlen):
        if (sum + d[i] > budget):
            break
        sum += d[i]
        i += 1
    answer = i
    return answer
