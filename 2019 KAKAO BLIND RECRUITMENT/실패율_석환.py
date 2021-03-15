def solution(N, stages):
    ans, cnt = [], [0] * (N+2)

    for i in range(len(stages)):
        cnt[stages[i]] += 1

    for i in range(1,N+1):
        finish, cellenger = cnt[i], cnt[i]
        for j in range(i+1,len(cnt)):
            finish += cnt[j]
        if finish != 0:
            fail = cellenger / finish
        else:
            fail = 0
        ans.append((fail,i))
    ans.sort(key=lambda x:-x[0])
    ans = [idx[1] for idx in ans]

    return ans

print(solution(5,[2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4,[4,4,4,4,4]))