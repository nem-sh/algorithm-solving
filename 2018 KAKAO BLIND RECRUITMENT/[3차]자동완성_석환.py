def solution(words):
    ans = 0
    words.sort()

    for i in range(len(words)):
        if i == 0:
            word1, word2 = words[i],words[i+1]
        elif i > 0 and i != len(words)-1:
            word0, word1, word2 = words[i-1], words[i], words[i+1]
        elif i == len(words)-1:
            word1, word2 = words[i], words[i-1]
        res,cnt = 0,0

        if i > 0:
            for j in range(len(word1)):
                if j < len(word0):
                    cnt += 1
                    if word1[j] != word0[j]:
                        break
                else:
                    cnt += 1
                    break
            if res < cnt:
                res = cnt

        cnt = 0
        for i in range(len(word1)):
            if i < len(word2):
                cnt += 1
                if word1[i] != word2[i]:
                    break
            else:
                cnt += 1
                break
        if res < cnt:
            res = cnt
        ans += res

    return ans

print(solution(["go","gone","guild"]))
print(solution(["abc","def","ghi","jklm"]))
print(solution(["word","war","warrior","world"]))