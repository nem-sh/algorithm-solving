from itertools import combinations
from collections import Counter


def solution(orders, course):
    answer = []
    for i in course:
        tmp = []
        for order in orders:
            tmp += combinations(sorted(order), i)
        cnt = Counter(tmp)
        if len(cnt) != 0 and max(cnt.values()) != 1:
            for j in cnt:
                if cnt[j] == max(cnt.values()):
                    answer.append(''.join(j))
    answer.sort()
    return answer
