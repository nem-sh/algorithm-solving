def solution(dartResult):
    answer = []
    n = ''
    for i in dartResult:
        if i.isnumeric():
            n += i
        elif i == 'S':
            answer.append(int(n) ** 1)
            n = ''
        elif i == 'D':
            answer.append(int(n) ** 2)
            n = ''
        elif i == 'T':
            answer.append(int(n) ** 3)
            n = ''
        elif i == '*':
            if len(answer) > 1:
                answer[-2] *= 2
            answer[-1] *= 2
        elif i == '#':
            answer[-1] *= -1
    return sum(answer)
