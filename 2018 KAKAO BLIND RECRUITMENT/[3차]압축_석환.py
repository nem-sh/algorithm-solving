def solution(msg):
    answer = []
    dic = {}

    for i in range(65,91):
        dic[chr(i)] = i-64

    pos = 0
    for i in range(len(msg)):
        if i < pos:
            continue
        for j in range(i+1,len(msg)+1):
            pos = j-1
            if msg[i:j] in dic:
                if j == len(msg):
                    idx = dic.get(msg[i:j])
                    answer.append(idx)
                    pos = j
                continue
            else:
                idx = dic.get(msg[i:j-1])
                answer.append(idx)
                dic[msg[i:j]] = len(dic)+1
                break

    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
print(solution('ABABABABABABABAB'))