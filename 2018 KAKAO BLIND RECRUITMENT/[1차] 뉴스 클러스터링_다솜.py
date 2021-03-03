def solution(str1, str2):
    str1 = [str1[i:i + 2].lower() for i in range(len(str1) - 1) if str1[i:i + 2].isalpha()]
    str2 = [str2[i:i + 2].lower() for i in range(len(str2) - 1) if str2[i:i + 2].isalpha()]

    if not str1 and not str2:
        return 65536
    ans1 = sum([min(str1.count(i), str2.count(i)) for i in list(set(str1) & set(str2))])
    ans2 = sum([max(str1.count(i), str2.count(i)) for i in list(set(str1) | set(str2))])
    return int(ans1 / ans2 * 65536)
