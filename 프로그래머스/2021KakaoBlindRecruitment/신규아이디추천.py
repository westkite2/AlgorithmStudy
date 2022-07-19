def solution(new_id):
    answer = ''
    answer = new_id.lower()
    for i in answer:
        if i.isalpha() == False and i.isdigit() == False:
            if i not in ("-", "_", "."):
                answer = answer.replace(i, "")
        answer = answer.replace("..", ".")
    if answer[0] == ".": answer = answer[1:]
    if answer[-1:] == ".": answer = answer[:-1]
    if len(answer) == 0: answer += "a"
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1:] == ".": answer = answer[:-1]
    while len(answer) <= 2:
        answer += answer[-1]
    return answer
