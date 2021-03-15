def func(m,n,board):
    tmp = set()
    for i in range(1, n):
        for j in range(1, m):
            if board[i][j] == board[i-1][j] == board[i][j-1] == board[i-1][j-1] != 0:
                tmp.update([(i, j), (i-1, j), (i, j-1), (i-1, j-1)])
            
    for i, j in tmp:
        board[i][j] = 0
        
    for i in range(n):
        board[i] = [0] * board[i].count(0) + [j for j in board[i] if j != 0]
    
    return len(tmp)

def solution(m, n, board):
    answer = 0
    board = list(map(list, zip(*board)))
    while 1:
        tmp = func(m, n, board)
        if tmp == 0:
            return answer
        answer += tmp
