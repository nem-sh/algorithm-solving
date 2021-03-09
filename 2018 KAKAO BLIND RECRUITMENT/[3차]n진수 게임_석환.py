def solution(n, t, m, p):
    tube = ''
    pos = 0
    nxt = 1
    nums = 0
    while len(tube) < t:
        if nums == 0:
            num = '0'
        else:
            num = ''
            b = nums
            while 1:
                a = b % n
                b = int(b/n)
                if a < 10:
                    num = str(a) + num
                elif 10<=a<=15:
                    a = chr(a+55)
                    num = a + num
                if b == 0:
                    break

        if nxt == p:
            tube += num[pos]
            nxt += 1
            pos += 1
        else:
            nxt += 1
            pos += 1

        if pos == len(num):
            pos = 0
            nums += 1

        if nxt > m:
            nxt = 1

    return tube

print(solution(2,4,2,1))
print(solution(16,16,2,1))
print(solution(16,16,2,2))