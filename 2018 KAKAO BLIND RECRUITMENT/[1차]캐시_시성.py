def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        return len(cities) * 5
    cache_li = []
    for city in cities:
        city_lower = city.lower()
        for i in range(len(cache_li)):
            if cache_li[i] == city_lower:
                answer += 1
                cache_li.append(cache_li.pop(i))
                break
        else:
            answer += 5
            if 0 <len(cache_li) == cacheSize:
                cache_li.pop(0)
            cache_li.append(city_lower)

    return answer