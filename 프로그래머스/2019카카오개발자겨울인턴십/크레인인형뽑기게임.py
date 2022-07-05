def solution(board, moves):
    answer = 0
    basket = []
    height = -1
    for j in moves:
        for i in range(len(board)):
            if board[i][j-1] != 0:
                basket.append(board[i][j-1])
                board[i][j-1] = 0
                if len(basket) > 1:
                    if basket[-1] == basket[-2]:                        
                        basket.pop()
                        basket.pop()
                        answer += 2
                break
    return answer
