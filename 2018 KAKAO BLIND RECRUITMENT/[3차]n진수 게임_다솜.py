def solution(n, t, m, p):
    answer = '0'
    nums = '0123456789ABCDEF'
    num = 1
    while t * m > len(answer):
        tmp = num
        ans = ''
        while tmp:
            ans = nums[tmp % n] + ans
            tmp //= n
        answer += ans
        num += 1
    return answer[p-1:t*m:m]
