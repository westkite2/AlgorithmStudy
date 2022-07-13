from collections import defaultdict

def solution(id_list, report, k):
    answer = []
    result = defaultdict(int)
    accused = defaultdict(list)
    count = defaultdict(int)
    for case in set(report):
        a, b = case.split()
        accused[a] += [b]
        count[b] += 1
    for user in id_list:
        if count[user] >= k:
            for users in id_list:
                if user in accused[users]:
                    result[users] += 1
    for user in id_list:
        answer.append(result[user])
    return answer

#other solution
'''
def solution(id_list, report, k):
    answer = [0] * len(id_list)
    accused = {x:0 for x in id_list}
    
    for case in set(report):
        accused[case.split()[1]] += 1
    for case in set(report):
        if accused[case.split()[1]] >= k:
            answer[id_list.index(case.split()[0])] += 1
    return answer
'''
