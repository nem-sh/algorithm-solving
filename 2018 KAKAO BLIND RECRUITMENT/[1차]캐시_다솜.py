def solution(cacheSize, cities):
    answer = 0
    cache = []
    for i in cities:
        if cacheSize == 0:
            return len(cities) * 5

        if i.lower() in cache:
            answer += 1
            cache.pop(cache.index(i.lower()))
        else:
            answer += 5

        if len(cache) == cacheSize:
            cache.pop(0)
            cache.append(i.lower())
        else:
            cache.append(i.lower())

    return answer
