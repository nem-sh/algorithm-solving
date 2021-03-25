def solution(record):
    answer=[]
    nickname = {}
    for i in [i.split(' ') for i in record]:
        if i[0] != 'Leave':
            nickname[i[1]] = i[2]
    for i in [i.split(' ') for i in record]:
        if i[0] == 'Enter':
            answer.append(nickname[i[1]] + '님이 들어왔습니다.')
        if i[0] == 'Leave':
            answer.append(nickname[i[1]] + '님이 나갔습니다.')
    return answer
