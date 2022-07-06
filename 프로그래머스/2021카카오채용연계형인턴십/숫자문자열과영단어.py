#처음에 작성한 것

'''
def solution(s):
    answer = ''
    dic = {0:"zero", 1:"one", 2:"two", 3: "three", 4: "four",
          5: "five", 6:"six", 7:"seven", 8: "eight", 9: "nine"}
    lens = len(s)
    i=0
    while i<lens:
        if s[i] >= '0' and s[i] <= '9':
            answer += s[i]
            i += 1
        else:
            for j in range(10):
                if s[i]==dic[j][0] and s[i+1]==dic[j][1]:
                    answer += str(j)
                    i += len(dic[j])
                    break
                    
    return int(answer)
'''

#수정한 것

dic = {0:"zero", 1:"one", 2:"two", 3: "three", 4: "four",
          5: "five", 6:"six", 7:"seven", 8: "eight", 9: "nine"}

def solution(s):
    answer = s
    for key, value in dic.items():
            answer = answer.replace(value, str(key))
    return int(answer)
