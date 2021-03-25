import heapq


def solution(n, s, a, b, fares):
    answer = 1e9
    lst = [[] for _ in range(n + 1)]
    for fare in fares:
        lst[fare[0]].append([fare[1], fare[2]])
        lst[fare[1]].append([fare[0], fare[2]])

    def func(st, ed):
        visit = [1e9] * (n + 1)
        visit[st] = 0
        heap = []
        heapq.heappush(heap, [0, st])
        while heap:
            time, x = heapq.heappop(heap)
            if visit[x] < time:
                continue
            for y, t in lst[x]:
                tmp = t + time
                if visit[y] > tmp:
                    visit[y] = tmp
                    heapq.heappush(heap, [tmp, y])
        return visit[ed]

    for i in range(1, n + 1):
        answer = min(answer, func(s, i) + func(i, a) + func(i, b))
    return answer
