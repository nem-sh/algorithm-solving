from collections import deque


def solution(board):
    d = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def bfs(start):
        n = len(board)
        Q = deque()
        Q.append((start, 0))
        visit = set()
        while Q:
            robots, cnt = Q.popleft()
            visit.add(robots)
            r1, c1, r2, c2 = robots[0], robots[1], robots[2], robots[3]
            if r2 == n - 1 and c2 == n - 1:
                return cnt

            # 이동
            for i in range(4):
                nr1, nc1, nr2, nc2 = r1 + d[i][0], c1 + d[i][1], r2 + d[i][0], c2 + d[i][1]
                if 0 <= nr1 < n and 0 <= nr2 < n and 0 <= nc1 < n and 0 <= nc2 < n:
                    if board[nr1][nc1] == 0 and board[nr2][nc2] == 0 and (nr1, nc1, nr2, nc2) not in visit:
                        visit.add((nr1, nc1, nr2, nc2))
                        Q.append(((nr1, nc1, nr2, nc2), cnt + 1))

            # 가로 회전
            if r1 == r2:
                if 0 <= r1 + 1 < n:
                    if board[r1 + 1][c1] == 0 and board[r2 + 1][c2] == 0:
                        if (r1, c1, r1 + 1, c1) not in visit:
                            visit.add((r1, c1, r1 + 1, c1))
                            Q.append(((r1, c1, r1 + 1, c1), cnt + 1))
                        if (r2, c2, r2 + 1, c2) not in visit:
                            visit.add((r2, c2, r2 + 1, c2))
                            Q.append(((r2, c2, r2 + 1, c2), cnt + 1))

                if 0 <= r1 - 1 < n:
                    if board[r1 - 1][c1] == 0 and board[r2 - 1][c2] == 0:
                        if (r1 - 1, c1, r1, c1) not in visit:
                            visit.add((r1 - 1, c1, r1, c1))
                            Q.append(((r1 - 1, c1, r1, c1), cnt + 1))
                        if (r2 - 1, c2, r2, c2) not in visit:
                            visit.add((r2 - 1, c2, r2, c2))
                            Q.append(((r2 - 1, c2, r2, c2), cnt + 1))

            # 세로 회전
            else:
                if 0 <= c1 + 1 < n:
                    if board[r1][c1 + 1] != 1 and board[r2][c2 + 1] != 1:
                        if (r1, c1, r1, c1 + 1) not in visit:
                            visit.add((r1, c1, r1, c1 + 1))
                            Q.append(((r1, c1, r1, c1 + 1), cnt + 1))
                        if (r2, c2, r2, c2 + 1) not in visit:
                            visit.add((r2, c2, r2, c2 + 1))
                            Q.append(((r2, c2, r2, c2 + 1), cnt + 1))

                if 0 <= c1 - 1 < n:
                    if board[r1][c1 - 1] != 1 and board[r2][c2 - 1] != 1:
                        if (r1, c1 - 1, r1, c1) not in visit:
                            visit.add((r1, c1 - 1, r1, c1))
                            Q.append(((r1, c1 - 1, r1, c1), cnt + 1))
                        if (r2, c2 - 1, r2, c2) not in visit:
                            visit.add((r2, c2 - 1, r2, c2))
                            Q.append(((r2, c2 - 1, r2, c2), cnt + 1))

    return bfs((0, 0, 0, 1))
