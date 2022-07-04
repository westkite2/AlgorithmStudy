def solution(numbers, hand):
    answer = ''
    keypad = {1:(0,0), 2:(0,1), 3:(0,2),
             4:(1,0), 5:(1,1), 6:(1,2),
             7:(2,0), 8:(2,1), 9:(2,2),
             "*":(3,0), 0:(3,1), "#":(3,2)}
    left = keypad["*"]
    right = keypad["#"]

    for i in numbers:
        cur = keypad[i]
        if i in (1, 4, 7):
            answer += "L"
            left = cur
        elif i in (3, 6, 9):
            answer += "R"
            right = cur
        else:
            distL = abs(left[0] - cur[0]) + abs(left[1]-cur[1])
            distR = abs(right[0] - cur[0]) + abs(right[1]-cur[1])
            if distL == distR:
                if hand=="right":
                    answer+= "R"
                    right = cur
                else:
                    answer += "L"
                    left = cur
            elif distL < distR:
                answer += "L"
                left = cur
            else:
                answer += "R"
                right = cur
                
    return answer
