def check(time, li):
    st, ed = time, time + 1000
    res = 0
    for i in li:
        if i[0] < ed and i[1] >= st:
            res += 1
    return res


def solution(lines):
    lst, answer = [], 1
    for line in lines:
        date, time, second = line.split()
        h, m, n = time.split(':')
        ed = (int(h) * 3600 + int(m) * 60 + float(n)) * 1000
        st = ed - float(second[:-1]) * 1000 + 1
        lst.append([st, ed])

    for i in lst:
        answer = max(answer, check(i[0], lst), check(i[1], lst))

    return answer


# print(solution([
#     "2016-09-15 01:00:04.001 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]))
