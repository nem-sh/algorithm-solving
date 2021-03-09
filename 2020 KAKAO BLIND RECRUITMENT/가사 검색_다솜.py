def madeTrie(tri, tmp, word):
    tri[len(word)][0] += 1
    res = tmp
    for w in word:
        tmp.setdefault(w, [0, {}])
        tmp[w][0] += 1
        tmp = tmp[w][1]
    return res


def solution(words, queries):
    trie, rev_trie = {}, {}
    for word in words:
        trie.setdefault(len(word), [0, {}])
        rev_trie.setdefault(len(word), [0, {}])
        madeTrie(trie, trie[len(word)][1], word)
        madeTrie(rev_trie, rev_trie[len(word)][1], word[::-1])

    answer = []
    for query in queries:
        ans = 0
        if len(query) not in trie:
            answer.append(0)
        elif query.count('?') == len(query):
            if len(query) not in trie:
                answer.append(0)
            else:
                answer.append(trie[len(query)][0])
        elif query[0] == '?':
            if len(query) in rev_trie:
                query = query[::-1]
                tmp = rev_trie[len(query)][1]
                q = query[:query.find('?')]
                for i in range(len(q)):
                    if q[i] in tmp:
                        ans = tmp[q[i]][0]
                        tmp = tmp[q[i]][1]
                    else:
                        ans = 0
                        break
                answer.append(ans)
            else:
                answer.append(0)
        else:
            if len(query) in trie:
                q = query[:query.find('?')]
                tmp = trie[len(query)][1]
                for i in range(len(q)):
                    if q[i] in tmp:
                        ans = tmp[q[i]][0]
                        tmp = tmp[q[i]][1]
                    else:
                        ans = 0
                        break
                answer.append(ans)
            else:
                answer.append(0)
    return answer
