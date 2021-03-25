import heapq

def solution(n, s, a, b, fares):
    def check(st,ed):
        visited = [float('inf')] * (n+1)
        visited[st] = 0
        heap = []
        heapq.heappush(heap,[0,st])

        while heap:
            fare, now = heapq.heappop(heap)
            if visited[now] < fare:
                continue
            for nxt, f in nodes[now]:
                fa = f + fare
                if visited[nxt] > fa:
                    visited[nxt] = fa
                    heapq.heappush(heap,[fa,nxt])
        return visited[ed]


    nodes = [[] for _ in range(n+1)]
    min_fare = float('inf')

    for i in range(len(fares)):
        nodes[fares[i][0]].append((fares[i][1],fares[i][2]))
        nodes[fares[i][1]].append((fares[i][0],fares[i][2]))

    for i in range(1,n+1):
        min_fare = min(min_fare, check(s,i)+check(i,a)+check(i,b))

    return min_fare

print(solution(6,4,6,2,[[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]))
print(solution(7,3,4,1,[[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
print(solution(6,4,5,6,[[2,6,6], [6,3,7], [4,6,7], [6,5,11], [2,5,12], [5,3,20], [2,4,8], [4,3,9]]))