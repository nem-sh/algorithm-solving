import sys
N, Q = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(2**N)]
L = list(map(int, input().split()))

sys.setrecursionlimit((2**N)**2)


def cast_fire_storms(A, A_size, l, drc):
    fire_storm_size = 2**l
    if fire_storm_size != 1:
        for r in range(0, A_size, fire_storm_size):
            for c in range(0, A_size, fire_storm_size):
                cast_fire_storm(A, r, c, fire_storm_size, drc)

    melt(A, A_size, drc)


def cast_fire_storm(A, r, c, fire_storm_size, drc):

    while fire_storm_size:
        temp = [0] * (fire_storm_size - 1)
        for dr, dc in drc:
            for i in range(0, fire_storm_size-1):
                temp[i], A[r][c] = A[r][c], temp[i]
                r += dr
                c += dc
        for i in range(0, fire_storm_size-1):
            A[r][c+i] = temp[i]
        r += 1
        c += 1
        fire_storm_size -= 2


def melt(A, A_size, drc):
    melt_check = [[False] * A_size for _ in range(A_size)]
    for r in range(A_size):
        for c in range(A_size):
            cnt = 0
            for dr, dc in drc:
                rr = r + dr
                cc = c + dc
                if 0 <= rr < A_size and 0 <= cc < A_size:
                    if 0 < A[rr][cc]:
                        cnt += 1
            if cnt < 3:
                melt_check[r][c] = True

    for r in range(A_size):
        for c in range(A_size):
            if melt_check[r][c] and 0 < A[r][c]:
                A[r][c] -= 1


def dfs_check_max_ice(A, r, c, drc, check_already):
    if A[r][c] == 0:
        return 0
    check_already[r][c] = True
    ice_size = 1
    for dr, dc in drc:
        rr = r + dr
        cc = c + dc

        if 0 <= rr < A_size and 0 <= cc < A_size:
            if check_already[rr][cc]:
                continue
            ice_size += dfs_check_max_ice(A, rr, cc, drc, check_already)
    return ice_size


A_size = 2**N
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for l in L:
    cast_fire_storms(A, A_size, l, drc)

check_already = [[False] * A_size for _ in range(A_size)]
total_ice = 0
max_ice_size = 0
for r in range(A_size):
    for c in range(A_size):
        total_ice += A[r][c]
        if check_already[r][c]:
            continue
        max_ice_size = max(max_ice_size, dfs_check_max_ice(
            A, r, c, drc, check_already))
print(total_ice)
print(max_ice_size)
