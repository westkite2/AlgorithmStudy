def solution(id_list, report, k):
    answer = [0]*len(id_list)
    accused = [0]*len(id_list)
    report = set(report)
    for case in report:
        accused[id_list.index(case.split()[1])] += 1
    for case in report:
        if accused[id_list.index(case.split()[1])] >= k:
            answer[id_list.index(case.split()[0])] += 1
    return answers
