def solution(msg):
    dic = dict()
    for i in range(ord('A'), ord('Z') + 1):
        dic[chr(i)] = i - 64

    st, idx, l = 0, 0, 26
    ans = []
    while 1:
        idx += 1
        if msg[st:st + idx] not in dic:
            ans.append(dic[msg[st:st + idx - 1]])
            l += 1
            dic[msg[st:st + idx]] = l
            st += idx - 1
            idx = 0
        else:
            # msg 의 마지막 인덱스일때
            if st + idx - 1 == len(msg):
                ans.append(dic[msg[st:st + idx - 1]])
                break
    return ans
