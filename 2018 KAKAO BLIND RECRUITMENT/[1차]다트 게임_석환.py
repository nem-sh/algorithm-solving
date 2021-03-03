dartResult = '1D2S3T*'

def solution(dartResult):
    answer = []
    mul = ['S','D','T']
    back = 0

    for i in range(1,len(dartResult)):
        if dartResult[i] in mul:
            nxt = i
            num = int(dartResult[back:nxt])
            if dartResult[i] == 'D':
                num = num ** 2
            elif dartResult[i] == 'T':
                num = num ** 3
            answer.append(num)
            back = i+1
        elif dartResult[i] == '*':
            if len(answer) < 2:
                answer[0] *= 2
            else:
                answer[-2] *= 2
                answer[-1] *= 2
            back = i+1
        elif dartResult[i] == '#':
            answer[-1] *= -1
            back = i+1

    return sum(answer)

print(solution(dartResult))