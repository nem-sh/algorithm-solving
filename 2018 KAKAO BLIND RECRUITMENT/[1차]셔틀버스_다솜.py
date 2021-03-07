def solution(n, t, m, timetable):
    timetable = sorted([int(time[:2]) * 60 + int(time[3:]) for time in timetable])
    time = 60 * 9 + (n - 1) * t  # 9시 + 시간
    for i in range(n):
        if len(timetable) < m:  # 1번
            return "%02d:%02d" % (time // 60, time % 60)
        if i == n - 1:  # 2, 3, 4번
            if timetable[0] <= time:
                if len(timetable) < m:
                    for j in range(m-1, -1, -1):
                        if timetable[j] <= time:
                            time = max(timetable[j] - 1, time)
                            break
                else:
                    if timetable[m-1] <= time:
                        time = timetable[m-1] - 1
            return "%02d:%02d" % (time // 60, time % 60)
        for j in range(m):
            tmp_time = 60 * 9 + i * t
            if timetable[j] <= tmp_time:
                timetable.pop(0)
