def check(t,timeline):
    st,ed = t, t+1
    cnt = 0
    for tt in timeline:
        if tt[0] < ed and tt[1] >= st:
            cnt += 1
    return cnt

def solution(lines):
    timeline = []

    for line in lines:
        date, time, dur = line.split()
        h, m, s = time.split(':')
        ed = int(h)*3600 + int(m)*60 + float(s)
        st = round(ed - float(dur[:-1]) + 0.001,3)
        timeline.append((st,ed))
    timeline.sort(key=lambda x:x[0])

    ans = 0
    for t in timeline:
        ans = max(ans, check(t[0], timeline), check(t[1],timeline))

    return ans

print(solution([
"2016-09-15 01:00:04.001 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution( [
"2016-09-15 01:00:04.002 2.0s",
"2016-09-15 01:00:07.000 2s"
]))
print(solution([
"2016-09-15 20:59:57.421 0.351s",
"2016-09-15 20:59:58.233 1.181s",
"2016-09-15 20:59:58.299 0.8s",
"2016-09-15 20:59:58.688 1.041s",
"2016-09-15 20:59:59.591 1.412s",
"2016-09-15 21:00:00.464 1.466s",
"2016-09-15 21:00:00.741 1.581s",
"2016-09-15 21:00:00.748 2.31s",
"2016-09-15 21:00:00.966 0.381s",
"2016-09-15 21:00:02.066 2.62s"
]))