def make_combined_set(string):
    combined_set = []
    for idx in range(len(string)-1):
        if string[idx].isalpha() and string[idx+1].isalpha():
            combined_set.append(ord(string[idx].upper())*26+ord(string[idx+1].upper()))
    return combined_set


def solution(str1, str2):
    str1_combined = sorted(make_combined_set(str1))
    str2_combined = sorted(make_combined_set(str2))
    cnt_union = 0
    cnt_inter = 0
    str1_idx = 0
    str2_idx = 0

    while len(str1_combined) > str1_idx and len(str2_combined) >str2_idx:
        if str1_combined[str1_idx] == str2_combined[str2_idx]:
            cnt_inter +=1
            cnt_union +=1
            str1_idx +=1
            str2_idx +=1
        elif str1_combined[str1_idx] < str2_combined[str2_idx]:
            cnt_union += 1
            str1_idx+=1
        else:
            cnt_union +=1
            str2_idx +=1

    cnt_union += len(str1_combined)+len(str2_combined)-str1_idx-str2_idx

    if len(str1_combined)+len(str2_combined) == 0:
        answer = 65536
    else:
        answer = int(cnt_inter / cnt_union * 65536)

    return answer

print(solution('FRANCE','french'))