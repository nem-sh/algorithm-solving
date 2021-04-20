import sys
sys.setrecursionlimit(500**2)

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]

drc = [(-1, 0), (0, -1), (1, 0), (0, 1)]
check_already = [[False] * N for _ in range(N)]
tornado_info = [[(-2, 0, 5), (-1, -1, 10), (-1, 1, 10), (0, -2, 2), (0, -1, 7), (0, 1, 7), (0, 2, 2), (1, -1, 1), (1, 1, 1)],
                [(0, -2, 5), (1, -1, 10), (-1, -1, 10), (2, 0, 2),
                 (1, 0, 7), (-1, 0, 7), (-2, 0, 2), (1, 1, 1), (-1, 1, 1)],
                [(2, 0, 5), (1, 1, 10), (1, -1, 10), (0, -2, 2), (0, -1, 7),
                 (0, 1, 7), (0, 2, 2), (-1, -1, 1), (-1, 1, 1)],
                [(0, 2, 5), (-1, 1, 10), (1, 1, 10), (2, 0, 2), (1, 0, 7), (-1, 0, 7), (-2, 0, 2), (1, -1, 1), (-1, -1, 1)]]


def move(A, drc, check_already, tornado_info, r, c, drc_idx):
    answer = 0
    check_already[r][c] = True
    drc_next_idx = drc_idx + 1 if drc_idx != 3 else 0
    dr, dc = drc[drc_next_idx]
    rr = r + dr
    cc = c + dc

    if (not (0 <= rr < N and 0 <= cc < N)) or check_already[rr][cc]:
        dr, dc = drc[drc_idx]
        rr = r + dr
        cc = c + dc
        drc_next_idx = drc_idx
        if not (0 <= rr < N and 0 <= cc < N):

            return answer

    answer += tornado(A, drc, tornado_info, rr, cc, drc_next_idx)
    answer += move(A, drc, check_already, tornado_info,
                   rr, cc, drc_next_idx)

    return answer


def tornado(A, drc, tornado_info, r, c, drc_idx):

    sand_total = 0
    answer = 0

    for dr, dc, n in tornado_info[drc_idx]:

        this_sand = A[r][c] * n // 100
        sand_total += this_sand
        rr = r+dr
        cc = c+dc

        if not (0 <= rr < N and 0 <= cc < N):

            answer += this_sand
        else:

            A[rr][cc] += this_sand

    dr, dc = drc[drc_idx]
    rr = r+dr
    cc = c+dc
    if not (0 <= rr < N and 0 <= cc < N):

        answer += A[r][c] - sand_total
    else:

        A[rr][cc] += A[r][c] - sand_total

    A[r][c] = 0
    return answer


answer = move(A, drc, check_already, tornado_info, N//2,  N//2, 0,)
print(answer)
