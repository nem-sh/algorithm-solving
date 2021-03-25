def solution(n, arr1, arr2):
    answer = []

    for i in range(n):
        tmp = [0] * n
        j = 0
        while arr1[i] > 0:
            tmp[j] = arr1[i] % 2
            arr1[i] //= 2
            j += 1
        j = 0
        while arr2[i] > 0:
            if tmp[j] == 0:
                tmp[j] = arr2[i] % 2
            arr2[i] //= 2
            j += 1

        ans = ''
        for j in range(n-1,-1,-1):
            if tmp[j] == 1:
                ans += '#'
            else:
                ans += ' '
        answer.append(ans)
    return answer
