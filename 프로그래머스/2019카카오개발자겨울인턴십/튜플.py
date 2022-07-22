def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    tmp = [x for x in s]
    tmp = sorted(tmp, key = len)
    for i in tmp:
        for j in i.split(','):
            if int(j) not in answer:
                answer.append(int(j))
    return answer
