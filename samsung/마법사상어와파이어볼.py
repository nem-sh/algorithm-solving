N, M, K = map(int, input().split())
field = [[None] * N for _ in range(N)]

for _ in range(M):
    r, c, m, s, d = map(int, input.split())

drc = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
print(field)
