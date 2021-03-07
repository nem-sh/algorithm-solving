def solution(words):
    trie = {}
    for word in words:
        tmp = trie
        for w in word:
            tmp.setdefault(w, [0, {}])
            tmp[w][0] += 1
            tmp = tmp[w][1]

    ans = 0
    for word in words:
        tmp = trie
        for i in range(len(word)):
            if tmp[word[i]][0] == 1:
                break
            tmp = tmp[word[i]][1]
        ans += i + 1
    return ans
