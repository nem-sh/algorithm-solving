def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()]
    str2 = [str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()]

    if (not str1 and not str2) or str1 == str2:
        return 65536

    ans1 = 0
    for i in list(set(str1) & set(str2)):
        ans1 += min(str1.count(i), str2.count(i))

    ans2 = 0
    for i in list(set(str1) | set(str2)):
        ans2 += max(str1.count(i), str2.count(i))

    answer = int(ans1/ans2*65536)

    return answer

print(solution('FRANCE','french'))
print(solution('handshake','shake hands'))
print(solution('aa1+aa2', 'AAAA12'))
print(solution('E=M*C^2', 'e=m*c^2'))