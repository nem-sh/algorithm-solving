def solution(N, stages):
    answer = {}
    l = len(stages)
    for i in range(1, N + 1):
        if l:
            answer[i] = stages.count(i) / l
        else:
            answer[i] = 0
        l -= stages.count(i)
    return sorted(answer, key=lambda x:answer[x], reverse=True)
