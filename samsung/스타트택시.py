from collections import deque

N, M, fuel = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())
taxi = (r-1, c-1)
customers = []
customers_dst = []

for _ in range(M):
    r, c, dst_r, dst_c = map(int, input().split())
    customers.append((r-1, c-1))
    customers_dst.append((dst_r-1, dst_c-1))


drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def move(field, r, c, dst_r, dst_c, drc):
    q = deque([(r, c, 0)])
    visited = [[False] * N for _ in range(N)]

    while q:
        r, c, distance = q.popleft()
        if r == dst_r and c == dst_c:
            return distance

        for dr, dc in drc:
            rr = r+dr
            cc = c+dc
            if 0 <= rr < N and 0 <= cc < N:
                if visited[rr][cc] == False and field[rr][cc] == 0:
                    visited[rr][cc] = True
                    q.append((rr, cc, distance+1))

    return -1


customers_check = [False] * M
for _ in range(M):
    min_distance = N**3
    selec_ted_customer_idx = -1
    r, c = taxi
    for customer_idx in range(M):
        if customers_check[customer_idx]:
            continue
        dst_r, dst_c = customers[customer_idx]
        if abs(r-dst_r) + abs(c-dst_c) > min_distance:
            continue
        distance = move(field, r, c, dst_r, dst_c, drc)
        if distance == -1:
            min_distance = -1
            break
        if min_distance >= distance:
            if min_distance == distance:
                rr, cc = customers[selected_customer_idx]
                if dst_r > rr or (dst_r == rr and dst_c > cc):
                    continue

            selected_customer_idx = customer_idx
            min_distance = distance

    customers_check[selected_customer_idx] = True
    if min_distance == -1:
        fuel = -1
        break

    fuel -= min_distance

    r, c = customers[selected_customer_idx]
    dst_r, dst_c = customers_dst[selected_customer_idx]

    distance = move(field, r, c, dst_r, dst_c, drc)
    if distance == -1:
        fuel = -1
        break
    if fuel < distance:
        fuel = -1
        break
    fuel += distance
    taxi = (dst_r, dst_c)

print(fuel)
