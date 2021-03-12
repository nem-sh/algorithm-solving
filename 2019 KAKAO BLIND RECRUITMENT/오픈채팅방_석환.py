def solution(record):
    ans = []
    uid = dict()

    for re in record:
        if re[0] != 'L':
            s, i, n = re.split()
            uid[i] = n

    for re in record:
        r = re.split()
        name = uid.get(r[1])
        if r[0] == 'Enter':
            ans.append('{}님이 들어왔습니다.'.format(name))
        elif r[0] == 'Leave':
            ans.append('{}님이 나갔습니다.'.format(name))

    return ans

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))