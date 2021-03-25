from itertools import combinations
from collections import defaultdict


def solution(info, query):
    dic = defaultdict(list)
    for i in info:
        rule, score = i.split(' ')[:-1], i.split(' ')[-1]
        for num in range(5):
            for r in combinations(rule, num):
                dic[''.join(r)].append(int(score))

    for key in dic:
        dic[key].sort()

    answer = []
    for q in query:
        tmp = q.replace(' and ', '').replace('-', '')
        rule, score = tmp.split(' ')[0], tmp.split(' ')[1]
        if rule in dic:
            temp = dic[rule]
            if temp:
                st, ed = 0, len(temp) - 1
                while st <= ed:
                    mid = (st + ed)//2
                    if temp[mid] >= int(score):
                        ed = mid - 1
                    else:
                        st = mid + 1
                answer.append(len(temp) - st)
        else:
            answer.append(0)
    return answer
