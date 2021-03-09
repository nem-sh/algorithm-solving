dr = [1,0,1]
dc = [0,1,1]

def solution(m, n, board):
    def reload():
        for i in range(-1,-m,-1):
            for j in range(n):
                if new[i][j] == '':
                    for k in range(i-1,-m-1,-1):
                        if new[k][j] != '':
                            new[i][j], new[k][j] = new[k][j], new[i][j]
                            break

        return

    def earse(answer):
        for i in range(m):
            for j in range(n):
                if visited[i][j] == 1:
                    if new[i][j] != '':
                        new[i][j] = ''
                        answer += 1
                    for a in range(3):
                        nr = i + dr[a]
                        nc = j + dc[a]
                        if 0<=nr<m and 0<=nc<n:
                            if new[nr][nc] != '':
                                new[nr][nc] = ''
                                answer += 1
        return answer

    def check(r,c,char):
        cnt = 1

        for a in range(3):
            nr = r + dr[a]
            nc = c + dc[a]
            if 0<=nr<m and 0<=nc<n:
                if new[nr][nc] == char:
                    cnt += 1
        if cnt == 4:
            visited[r][c] = 1
        return

    answer = 0
    new = [['']*n for _ in range(m)]
    visited = [[0]*n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            new[i][j] = board[i][j]

    flag = True

    while flag:
        for i in range(m):
            for j in range(n):
                if new[i][j] != '':
                    check(i,j,new[i][j])

        for i in range(m):
            if 1 not in visited[i]:
                flag = False
            else:
                flag = True
                break

        if not flag:
            break

        answer = earse(answer)
        visited = [[0]*n for _ in range(m)]
        reload()

    return answer

print(solution(6,6,["AABBEE","AAAEEE","VAAEEV","AABBEE","AACCEE","VVCCEE" ]))
print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))
print(solution(6,6,["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))