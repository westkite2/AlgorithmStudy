def solution(board, moves):
    answer = 0
    bucket = []
    for i in range(len(moves)):
        for r in range(len(board)):
            if board[r][moves[i]-1] != 0:
                if bucket and board[r][moves[i]-1] == bucket[-1]:
                    bucket.pop()
                    answer += 2
                else:
                    bucket.append(board[r][moves[i]-1])
                board[r][moves[i]-1] = 0
                break
    return answer


