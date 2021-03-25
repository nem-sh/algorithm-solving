# from itertools import combinations

# def solution(relation):
#     answer = 0
#     l = len(relation[0])
#     stack = []
#     for i in range(1, l+1):
#         relate = combinations(range(l), i)
#         for j in relate:
#             tmp = [tuple(r[k] for k in j) for r in relation]
#             if len(set(tmp)) == len(relation):
#                 stack.append(j)

#     answer = []
#     i = cnt = 0
#     while 1:
#         visit = [0] * len(stack)
#         if 0 not in visit:
#             break
#         visit[i] = 1
#         for j in range(i+1, len(stack)):
#             if visit[j] == 0 and len(stack[i]) == len(set(stack[i]) & set(stack[j])):
#                 visit[j] = 1
#             else:
#                 answer.append(stack[j])
#         stack = answer
#         answer = []
#         cnt += 1
#     return cnt

from itertools import combinations


def solution(relation):
    combi = []
    for i in range(1, len(relation[0]) + 1):
        combi += list(combinations(range(len(relation[0])), i))
    
    res = []
    for com in combi:
        tmp = [tuple([re[c] for c in com]) for re in relation]
        if len(relation) == len(set(tmp)):
            res.append(com)
    
    answer = set(res)
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            if len(res[i]) == len(set(res[i]) & set(res[j])):
                answer.discard(res[j])
    return len(answer)
