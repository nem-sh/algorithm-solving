from itertools import permutations


def solution(n, weak, dist):
    if len(weak) == 1:
        return 1

    w, d = len(weak), len(dist)
    answer = d + 1
    weak += [i + n for i in weak]

    for i in range(w):
        start = weak[i:i + w]
        for rule in permutations(dist, d):
            idx, cnt = 0, 1
            tmp = start[0] + rule[idx]
            for j in range(w):
                if start[j] > tmp:
                    cnt += 1
                    if cnt > len(rule):
                        break
                    idx += 1
                    tmp = start[j] + rule[idx]
            answer = min(answer, cnt)

    if answer > d:
        return -1
    return answer
