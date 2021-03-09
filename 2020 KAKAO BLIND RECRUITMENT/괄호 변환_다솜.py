def divide(p):
    st = ed = 0
    for i in range(len(p)):
        if p[i] == '(':
            st += 1
        else:
            ed += 1
        if st == ed:
            return p[:i + 1], p[i + 1:]


def check(u):
    cnt = 0
    for i in u:
        if i == '(':
            cnt += 1
        else:
            cnt -= 1
        if cnt < 0:
            return False
    return True


def solution(p):
    if p == '':
        return ''

    u, v = divide(p)
    if check(u):
        return u + solution(v)
    else:
        answer = '(' + solution(v) + ')'
        for i in u[1:len(u) - 1]:
            if i == '(':
                answer += ')'
            else:
                answer += '('
        return answer