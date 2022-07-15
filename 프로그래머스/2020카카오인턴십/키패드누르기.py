def getDistance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def solution(numbers, hand):
    answer = ''
    coord = {1: (0,0), 2: (0,1), 3: (0,2),
            4: (1,0), 5: (1,1), 6: (1,2),
            7: (2,0), 8: (2,1), 9: (2,2),
            10: (3,0), 0: (3,1), 11: (3,2)}
    leftnow = coord[10]
    rightnow = coord[11]
    for num in numbers:
        if num in (1, 4, 7):
            answer += 'L'
            leftnow = coord[num]
        elif num in (3, 6, 9):
            answer += 'R'
            rightnow = coord[num]
        else:
            rightcost = getDistance(coord[num], rightnow)
            leftcost = getDistance(coord[num], leftnow)
            if rightcost > leftcost:
                answer += 'L'
                leftnow = coord[num]
            elif rightcost < leftcost:
                answer += 'R'
                rightnow = coord[num]
            else:
                if hand == 'right':
                    answer += 'R'
                    rightnow = coord[num]
                else:
                    answer += 'L'
                    leftnow = coord[num]                    
    return answer
