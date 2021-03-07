def find(m,de):
    for i in range(len(de)):
        if m[:] == de[i:i+len(m)]:
            return True

    return False

def solution(m, musicinfos):
    answer = []
    mm = []
    for i in range(len(m)):
        if m[i] == '#':
            continue
        elif i == len(m)-1:
            mm.append(m[i])
        elif m[i+1] == '#':
            mm.append(m[i]+m[i+1])
        elif m[i+1] != '#':
            mm.append(m[i])

    for music in musicinfos:
        st_time, ed_time, name, detail = music.split(',')
        dur_t = int(ed_time[:2])-int(st_time[:2])
        dur_m = int(ed_time[3:])-int(st_time[3:])
        dur_de = []

        for i in range(len(detail)):
            if detail[i] == '#':
                continue
            elif i == len(detail)-1:
                dur_de.append(detail[i])
            elif detail[i+1] == '#':
                dur_de.append(detail[i]+detail[i+1])
            elif detail[i+1] != '#':
                dur_de.append(detail[i])

        de = []
        tm = dur_t*60+dur_m
        for mi in range(tm):
            if mi >= len(dur_de):
                de.append(dur_de[mi%len(dur_de)])
            else:
                de.append(dur_de[mi])

        flag = find(mm,de)

        if flag:
            answer.append((tm,name))

    if len(answer) > 1:
        answer.sort(key=lambda x: -x[0])
        ans = answer[0][1]
    elif len(answer) == 1:
        ans = answer[0][1]
    else:
        ans = "(None)"

    return ans

print(solution("ABCDEFG",["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC",["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))