def solution(new_id):
    #answer = ''
    answer = new_id.lower()
    for i in answer:
        if i.isalpha() == False and i.isdigit()==False and i not in  ("-", "_", "."):
            answer = answer.replace(i,"")
        answer = answer.replace("..",".")
    if answer[0] == ".": answer = answer[1:]
    if answer[-1:] == ".": answer = answer[:-1:]
    if answer == "": answer += "a"
    if len(answer) >= 16: answer = answer [:15]
    if answer[-1:] == ".": answer = answer[:-1:]
    if len(answer) <= 2:
        while len(answer) != 3:
            answer += answer[-1:]
    return answer
