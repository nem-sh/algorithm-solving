from itertools import permutations
from collections import deque

answer = 1e9
cards = {}
di = [[0, -1], [0, 1], [-1, 0], [1, 0]]


def ctrl(board, x, y, i):
    di2 = [[x, 0], [x, 3], [0, y], [3, y]]
    aa, bb = x, y
    while 1:
        na, nb = aa + di[i][0], bb + di[i][1]
        if na < 0 or na >= 4 or nb < 0 or nb >= 4:
            return di2[i][0], di2[i][1]
        if board[na][nb] != 0:
            return na, nb
        aa, bb = na, nb


def bfs(board, a1, b1, a2, b2):
    visit = [[0] * 4 for _ in range(4)]
    visit[a1][b1] = 1
    if a1 == a2 and b1 == b2:
        return a2, b2, visit[a1][b1]
    Q = deque()
    Q.append([a1, b1])
    while Q:
        a, b = Q.popleft()
        for i in range(4):
            # ctrl 부터
            ma, mb = ctrl(board, a, b, i)
            if not visit[ma][mb]:
                visit[ma][mb] = visit[a][b] + 1
                if ma == a2 and mb == b2:
                    return ma, mb, visit[ma][mb]
                Q.append([ma, mb])

            # 그냥 이동
            na, nb = a + di[i][0], b + di[i][1]
            if 0 <= na < 4 and 0 <= nb < 4 and not visit[na][nb]:
                visit[na][nb] = visit[a][b] + 1
                if na == a2 and nb == b2:
                    return na, nb, visit[na][nb]
                Q.append([na, nb])


def func(board, x, y, rule, k, res):
    global answer
    if k == len(cards):
        answer = min(answer, res)
        return

    card = rule[k]
    x1, y1 = cards[card][0][0], cards[card][0][1]
    x2, y2 = cards[card][1][0], cards[card][1][1]

    # x1, y1 부터 방문
    r1, c1, res1 = bfs(board, x, y, x1, y1)
    r2, c2, res2 = bfs(board, r1, c1, x2, y2)
    board[x1][y1], board[x2][y2] = 0, 0
    func(board, r2, c2, rule, k + 1, res + res1 + res2)
    board[x1][y1], board[x2][y2] = card, card

    # x2, y2 부터 방문
    r1, c1, res1 = bfs(board, x, y, x2, y2)
    r2, c2, res2 = bfs(board, r1, c1, x1, y1)
    board[x1][y1], board[x2][y2] = 0, 0
    func(board, r2, c2, rule, k + 1, res + res1 + res2)
    board[x1][y1], board[x2][y2] = card, card


def solution(board, r, c):
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                cards.setdefault(board[i][j], [])
                cards[board[i][j]].append([i, j])

    for rules in permutations(cards.keys(), len(cards)):
        func(board, r, c, rules, 0, 0)
    return answer
